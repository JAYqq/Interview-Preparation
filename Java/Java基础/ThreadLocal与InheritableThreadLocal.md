# ThreadLocal

- 可以绑定值在本线程上，实现线程的私有变量
- 不可跨线程访问

## 关系分析

三层对象：

1. Thread
2. ThreadLocal
3. ThreadLocalMap
4. Entry

### ThreadLocal

- 与Thread无直接关系，是用于帮助Thread管理ThreadLocalMap的
- **一个线程内可以创建多个ThreadLocal**

### ThreadLocalMap

- ThreadLocal的内部类，也是Thread的成员

- 管理Entry数组

  ```java
  private Entry[] table;
  ```

- **一个线程只有一个ThreadLocalMap**

  ```java
  /* ThreadLocal values pertaining to this thread. This map is maintained
   * by the ThreadLocal class. */
  ThreadLocal.ThreadLocalMap threadLocals = null;
  ```

- ThreadLocalMap是使用线性探测解决哈希冲突，源码中在清除泄漏的Entry时，会进行rehash，防止数组的当前位置为null后，有hash冲突的Entry访问不到的问题。

### Entry

- ThreadLocalMap的基本单元
- **set和get的数据都是储存在Entry对象中**

## 行为分析

### get

```java
public T get() {
    Thread t = Thread.currentThread(); //获取当前Thread
    ThreadLocalMap map = getMap(t); //获取Thread绑定的ThreadLocalMap
    if (map != null) {
        ThreadLocalMap.Entry e = map.getEntry(this); //获取map的entry
        if (e != null) {
            @SuppressWarnings("unchecked")
            T result = (T)e.value;
            return result;
        }
    }
    return setInitialValue(); // 设置value为默认值null
}
```

- 这边默认值的设置是在get的时候设置的，像是懒加载

### set

```java
public void set(T value) {
    Thread t = Thread.currentThread();
    ThreadLocalMap map = getMap(t);
    if (map != null)
        map.set(this, value);
    else
        createMap(t, value);
}
```

## 相关问题

### 为什么要以数组形式储存值

问题主要是ThreadLocal的set和get都只能存一个值，为什么还要以数组形式储存

无论get还是set的过程，都是从当前的Thread中取出ThreadLocalMap然后进行取值和赋值，并且上面说了，一个Thread只有一个ThreadLocalMap，但是一个Thread可以有多个ThreadLocal，因此一个线程的多个ThreadLocal是共享一个ThreadLocalMap，也就是说不同ThreadLocal的赋值，都是存在一个map中，以ThreadLocal自己的hashcode为key，值为value存下来，所以需要数组。

参考：https://www.zhihu.com/question/279007680

### 为什么Entry的key要用弱引用保存ThreadLocal？

```java
static class Entry extends WeakReference<ThreadLocal<?>> {
    /** The value associated with this ThreadLocal. */
    Object value;

    Entry(ThreadLocal<?> k, Object v) {
        super(k);
        value = v;
    }
}
```

由于ThreadLocalMap对Thread来说是强引用，所以线程不结束，ThreadLocalMap一直不会被回收。而如果key是强引用，那么当ThreadLocal对象没用后，也会一直存在导致内存泄露，所以改为弱引用后，ThreadLocal对象就会被GC回收。

### 为什么ThreadLocal还有内存泄漏问题

改为了弱引用为什么还有内存泄漏，因为key对应的val还是强引用，即存在key为null，但value却有值的无效Entry。

而ThreadLocal有另外的措施，它有个方法：

```java
private int expungeStaleEntry(int staleSlot){}
```

作用是擦除某个下标的Entry（置为null，可以回收），同时检测整个Entry[]表中对key为null的Entry一并擦除，重新调整索引，在每次调用ThreadLocal的get、set、remove方法时都会执行。

### 最佳实践

- 在finally中手动调用remove方法清除Entry

# InheritableThreadLocal

其实和ThreadLoca的实现差不多，都是有ThreadLocalMap对ThreadLocal和value进行映射，Thread内部也是保留了：

```java
/*
     * InheritableThreadLocal values pertaining to this thread. This map is
     * maintained by the InheritableThreadLocal class.
     */
    ThreadLocal.ThreadLocalMap inheritableThreadLocals = null;
```

这个变量，保证一个线程只有一个inheritableThreadLocals对象

## 实现父子线程传值的原理

其实inheritableThreadLocals 相比于普通ThreadLocal可以实现传值，主要是因为，在创建Thread的时候 **一定会调用Thread.init方法**，而这个方法里面有一段代码：

```java
if (inheritThreadLocals && parent.inheritableThreadLocals != null)
    this.inheritableThreadLocals =
    ThreadLocal.createInheritedMap(parent.inheritableThreadLocals);
```

意思很简单，就是说如果父线程有inheritableThreadLocals对象切不为空，那么就把子线程的inheritableThreadLocals拷贝一份父线程的，其实主要是对tabel数组也就是存放entry的数组进行拷贝，这样父子的inheritableThreadLocals数据相同，就实现了父子线程的传值。

### 存在的问题

#### 线程池传值失效

我们期望的是，线程池中的线程可以都访问到父线程的值，但是inheritableThreadLocals却失效了，如下：

```java
public class Test01 {
    static ExecutorService executorService2 = Executors.newFixedThreadPool(1);
    static InheritableThreadLocal threadLocal = new InheritableThreadLocal();
    public static void main(String[] args) {
        threadLocal.set("set by parent");
        executorService2.submit(()->{
            System.out.println(threadLocal.get());
            threadLocal.set("threadlocal set by thread:"+Thread.currentThread().getName());
        });
        executorService2.submit(()->{
            try {
                Thread.sleep(100);
            }catch (InterruptedException e){
                e.printStackTrace();
            }
            System.out.println(threadLocal.get());
        });
    }
}
```

可以看到输出

```
set by parent
threadlocal set by thread:pool-2-thread-1
```

发现在子线程中改了值以后，后面进来的task就无法访问父线程的threadlocal了，因此存在隐患，又或者有如下问题：

```java
public class Test01 {
    static ExecutorService executorService2 = Executors.newFixedThreadPool(1);
    static InheritableThreadLocal threadLocal = new InheritableThreadLocal();
    public static void main(String[] args) {
        threadLocal.set("set by parent");
        executorService2.submit(()->{
            System.out.println(threadLocal.get());
        });
        System.out.println("线程池线程用完了");
        threadLocal.set("threadlocal set by thread:"+Thread.currentThread().getName()); //在主线程修改
        executorService2.submit(()->{
            try {
                Thread.sleep(100);
            }catch (InterruptedException e){
                e.printStackTrace();
            }
            System.out.println(threadLocal.get());
        });
    }
}
```

这一次不是在子线程中修改，而是在主线程中修改数据，结果发现

```
线程池线程用完了
set by parent
set by parent
```

主线程修改后进来的task没有获取到新的值，这也是问题

**原因分析**

原因在于InheritableThreadLocal是在创建线程的时候才会调用init方法去复制父线程的数据，但是线程池本身的理念就是线程复用，当线程池中任务数量大于核心线程后就会出现线程复用的情况，这个时候可是没有创建新线程，这就是本质原因。

**解决**

https://github.com/alibaba/transmittable-thread-local