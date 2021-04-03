# ThransmitedThreadLocal

首先记住：

ITL、TTL都是继承普通ThreadLocal，用的也是ThreadLocal.ThreadLocalMap

```java
import com.alibaba.ttl.TransmittableThreadLocal;
import com.alibaba.ttl.TtlRunnable;
import org.apache.commons.lang3.time.DateUtils;


import java.sql.Timestamp;
import java.text.SimpleDateFormat;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.Date;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicInteger;

public class ThransmitedThreadLocal {
    private static final AtomicInteger ID_SEQ = new AtomicInteger();
    private static final ExecutorService EXECUTOR = Executors.newFixedThreadPool(1, r -> new Thread(r, "TTL-TEST-" + ID_SEQ.getAndIncrement()));
    //⑴ 声明TransmittableThreadLocal类型的ThreadLocal
    private static TransmittableThreadLocal<String> THREAD_LOCAL = new TransmittableThreadLocal<>();
    public static void testThreadLocal() throws InterruptedException {
        try {
            //doSomething()...
            THREAD_LOCAL.set("set-task-init-value");
            //
            Runnable task1 = () -> {
                String manTaskCtx = THREAD_LOCAL.get();
                System.out.println("task1:" + Thread.currentThread() + ", get ctx:" + manTaskCtx);
                THREAD_LOCAL.set("task1-set-value");
            };
            EXECUTOR.submit(task1);

            //doSomething....
            TimeUnit.SECONDS.sleep(1);

            //⑵ 设置期望task2可获取的上下文
            THREAD_LOCAL.set("main-task-value");

            //⑶ task2的异步任务逻辑中期望获取⑵中的上下文
            Runnable task2 = () -> {
                String manTaskCtx = THREAD_LOCAL.get();
                System.out.println("task2:" + Thread.currentThread() + ", get ctx :" + manTaskCtx);
            };
            //⑷ 转换为TransmittableThreadLocal 增强的Runnable
            task2 = TtlRunnable.get(task2);
            EXECUTOR.submit(task2);
        }finally {
            THREAD_LOCAL.remove();
        }
    }
    public static void main(String[] args) throws InterruptedException {
        testThreadLocal();
    }
}
```

## CRR

是一个面向上下文传递设计的流程，通过这个流程的分析可以保证/证明 正确性。



TTL的set方法，由于TTL继承了ITL，所以set首先也会调用super.set，也就是ThreadLocal的set方法，并且，而TTL在此基础上，还调用了addThisToHolder方法，这个方法的作用是将这个TTL对象添加到当前线程的holder

### holder

```java
private static final InheritableThreadLocal<WeakHashMap<TransmittableThreadLocal<Object>, ?>> holder = new InheritableThreadLocal<WeakHashMap<TransmittableThreadLocal<Object>, ?>>() {
        protected WeakHashMap<TransmittableThreadLocal<Object>, ?> initialValue() {
            return new WeakHashMap();
        }
        protected WeakHashMap<TransmittableThreadLocal<Object>, ?> childValue(WeakHashMap<TransmittableThreadLocal<Object>, ?> parentValue) {
            return new WeakHashMap(parentValue);
        }
    };
```

holder是一个类级别的常量，**由于是常量，所以当前线程内部第一次初始化TTL时有且仅创建这一次holder**，所以它可以用来存储当前线程拥有的所有TTL对象。

这个holder重写了childValue方法，这个方法影响的是 createInheritedMap 这个方法，这个方法再ITL中是用来赋值父线程Map的。

### THREAD_LOCAL.set

这是上面代码的关键第一步，平平无奇。

```java
public class TransmittableThreadLocal<T> extends InheritableThreadLocal<T> implements TtlCopier<T>
```

```java
    public final void set(T value) {
        if (!this.disableIgnoreNullValueSemantics && null == value) {
            this.remove();
        } else {
            super.set(value);
            this.addThisToHolder();
        }
    }
```

TTL继承ITL，因此这个set本质上就是ThreadLocal的原生的set，只不过放到了Thread的ITL Map中，key变成了TTL，value还是一样。

然后addThisToHolder方法：

```java
   private void addThisToHolder() {
        if (!((WeakHashMap)holder.get()).containsKey(this)) {
            ((WeakHashMap)holder.get()).put(this, (Object)null);
        }
    }
```

这个方法作用是将当前Thread使用的TTL保留一份到holder中，那么保留的格式是什么？

上面holder是WeakHashMap<TransmittableThreadLocal<Object>, ?>为泛值的ITL，也就是说，holder保存的ThreadLocalMap是key为WeakHashMap<TransmittableThreadLocal<Object>, ?>，value为WeakHashMap的TLMap。

至此，从我们写代码：

```java
TransmittableThreadLocal<String> THREAD_LOCAL = new TransmittableThreadLocal<>();
```

之后，每次set都是在Thread的ITLMap中存一份（Key=TTL，Value=随便）。然后 **保存了一份TTL引用在holder中**，类型也是ITL，只不过这个ITL的Map比较特殊，Key=ITL，value=WeakHashMap，而这个value的key为TTL，value为null，**也就是说，这个holder的TLMap格式是这样的：**，

```java
{
	holder这个ITL对象:{
		"TTL_ONE:当前线程使用的第一个TTL":"(Object)null", 
		"TTL_TWO":当前线程使用的第二个TTL":"(Object)null",
		......
	}
}
```

**value为null是因为只需要保存一份TTL的引用就行了**

这就是addThisToHolder方法的作用。

上面简单介绍了TTL调用了set之后发生的事情以及原理，那么真正的capture阶段是从线程池submit之前，因为submit意味着线程就要被run了，因此一定要在这之前完成整个CRR

### C(Capture)

TtlRunnable 有一个对象

```java
private final AtomicReference<Object> capturedRef = new AtomicReference(Transmitter.capture());
```

调用了Transmitter.capture()，这个Transmit类命名很形象，因为它就是为了整个CRR。

```java
public static Object capture() {
    return new TransmittableThreadLocal.Transmitter.Snapshot(captureTtlValues(), captureThreadLocalValues());
}
```



首先看captureTtlValues

```java
private static HashMap<TransmittableThreadLocal<Object>, Object> captureTtlValues() {
    HashMap<TransmittableThreadLocal<Object>, Object> ttl2Value = new HashMap();
    Iterator var1 = ((WeakHashMap)TransmittableThreadLocal.holder.get()).keySet().iterator();

    while(var1.hasNext()) {
        TransmittableThreadLocal<Object> threadLocal = (TransmittableThreadLocal)var1.next();
        ttl2Value.put(threadLocal, threadLocal.copyValue());
    }
    
    return ttl2Value;
}
```

这边做的就是将holder中储存的当前线程使用的item（TTL:Object）拷贝到Snapshot.ttl2Value

然后是captureThreadLocalValues

```java
private static HashMap<ThreadLocal<Object>, Object> captureThreadLocalValues() {
    HashMap<ThreadLocal<Object>, Object> threadLocal2Value = new HashMap();
    Iterator var1 = threadLocalHolder.entrySet().iterator();

    while(var1.hasNext()) {
        Entry<ThreadLocal<Object>, TtlCopier<Object>> entry = (Entry)var1.next();
        ThreadLocal<Object> threadLocal = (ThreadLocal)entry.getKey();
        TtlCopier<Object> copier = (TtlCopier)entry.getValue();
        threadLocal2Value.put(threadLocal, copier.copy(threadLocal.get()));
    }

    return threadLocal2Value;
}
```

将threadLocalHolder中的ThreadLocal拷贝

**至此，一个task在执行run之前，就已经将父线程的所有的ThreadLocal拷贝到了capturedRef**

### R(Replay)

线程执行后，一定要先将父线程的所有ThreadLocal复原到本线程

#### 从哪到哪？

从capturedRef到子线程的ThreadLocalMap

首先task交给线程池之后要run了

```java
public void run() {
    Object captured = this.capturedRef.get();
    if (captured != null && (!this.releaseTtlValueReferenceAfterRun || this.capturedRef.compareAndSet(captured, (Object)null))) {
        Object backup = Transmitter.replay(captured);

        try {
            this.runnable.run();
        } finally {
            Transmitter.restore(backup);
        }

    } else {
        throw new IllegalStateException("TTL value reference is released after run!");
    }
}
```

可见run之前，要replay

```java
public static Object replay(@NonNull Object captured) {
    TransmittableThreadLocal.Transmitter.Snapshot capturedSnapshot = (TransmittableThreadLocal.Transmitter.Snapshot)captured;
    return new TransmittableThreadLocal.Transmitter.Snapshot(replayTtlValues(capturedSnapshot.ttl2Value), replayThreadLocalValues(capturedSnapshot.threadLocal2Value));
}
```

和capture一样返回一个Snapshot，包含了holder的TTL和普通threadlocal

然后看看replayTtlValues

```java
private static HashMap<TransmittableThreadLocal<Object>, Object> replayTtlValues(@NonNull HashMap<TransmittableThreadLocal<Object>, Object> captured) {
    HashMap<TransmittableThreadLocal<Object>, Object> backup = new HashMap();
    Iterator iterator = ((WeakHashMap)TransmittableThreadLocal.holder.get()).keySet().iterator(); //获取当前线程的holder

    while(iterator.hasNext()) {
        TransmittableThreadLocal<Object> threadLocal = (TransmittableThreadLocal)iterator.next();
        backup.put(threadLocal, threadLocal.get());
        if (!captured.containsKey(threadLocal)) { //如果当前线程holder里有父线程中没有的，就去掉，为的是保证父子线程TTL对象的一致性
            iterator.remove();
            threadLocal.superRemove();
        }
    }

    setTtlValuesTo(captured); //关键一步，将父线程的TTL保存到当前线程的ThreadLocalMap
    TransmittableThreadLocal.doExecuteCallback(true);
    return backup;
}
```

然后是setTtlValuesTo

```java
private static void setTtlValuesTo(@NonNull HashMap<TransmittableThreadLocal<Object>, Object> ttlValues) {
    Iterator var1 = ttlValues.entrySet().iterator();

    while(var1.hasNext()) {
        Entry<TransmittableThreadLocal<Object>, Object> entry = (Entry)var1.next();
        TransmittableThreadLocal<Object> threadLocal = (TransmittableThreadLocal)entry.getKey();
        threadLocal.set(entry.getValue());
    }

}
```

逻辑清晰，保存到当前线程的map

### R(Restore)

此时子线程已经run了，执行完以后，需要恢复现场为下次线程复用提供干净的场所，就像去看完球赛以后要带走所有垃圾一样。

```java
public static void restore(@NonNull Object backup) {
    TransmittableThreadLocal.Transmitter.Snapshot backupSnapshot = (TransmittableThreadLocal.Transmitter.Snapshot)backup;
    restoreTtlValues(backupSnapshot.ttl2Value);
    restoreThreadLocalValues(backupSnapshot.threadLocal2Value);
}

private static void restoreTtlValues(@NonNull HashMap<TransmittableThreadLocal<Object>, Object> backup) {
    TransmittableThreadLocal.doExecuteCallback(false);
    Iterator iterator = ((WeakHashMap)TransmittableThreadLocal.holder.get()).keySet().iterator();

    while(iterator.hasNext()) {
        TransmittableThreadLocal<Object> threadLocal = (TransmittableThreadLocal)iterator.next();
        if (!backup.containsKey(threadLocal)) {
            iterator.remove();
            threadLocal.superRemove();
        }
    }
    setTtlValuesTo(backup);
}
```

代码一目了然。

## 小结

### TTL解决的问题

ITL实现父子线程共享ThreadLoca是在初始化线程时，调用链为：new Thread()  ---->Thread()  -------> init()  --------> createInheritedMap，走到这才会复制父线程的Map。但是线程池会有线程复用的情况，导致无法触发createMap方法。TTL就是解决这个问题。

### TTL如何解决

有如下几个关键点：

#### 1.holder

保存当前线程使用过的TTL对象引用，便于拷贝

#### 2.capture

子线程执行之前会拷贝父线程的所有ThreadLocal到自己这

#### 3.replay

子线程执行前会重放拷贝对象到子线程的ThreadLocalMap

#### 4.restore

子线程执行完后清理与拷贝集合不一致的数据，并恢复子线程的Map与父线程一样。