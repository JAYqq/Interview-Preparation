## Threading多线程

### 基本运用

```python
from threading import Thread
def func(name):
    print(f"name:{name}")

thread1=Thread(target=func,args=("mason",))
thread2=Thread(target=func,args=("Juli",))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
```

简单粗暴，**注意点：单个传参需要逗号结尾**

### 使用类

```python
class MyClass(object):

    def func(self,name,sec):
        print('---开始---', name, '时间', ctime())
        sleep(sec)
        print('***结束***', name, '时间', ctime())

def main():
    # 创建 Thread 实例
    t1 = Thread(target=MyClass().func, args=(1, 1))
    t2 = Thread(target=MyClass().func, args=(2, 2))

    # 启动线程运行
    t1.start()
    t2.start()

    # 等待所有线程执行完毕
    t1.join()  # join() 等待线程终止，要不然一直挂起
    t2.join()

if __name__=="__main__":
    main()
```

join使得主线程等待子线程完成后才终止。

### 使用Thread派生类

```python
from threading import Thread
class MyThread(Thread):
    def __init__(self,func,args):
        Thread.__init__(self)
        self.func=func
        self.args=args
    def run(self):
        self.func(*self.args)
def func(name):
    print(f"name:{name}")
def main():
    thread1=MyThread(func,("mason",))
    thread2=MyThread(func,("July",))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
main()
```

### 获取返回值

```python
from threading import Thread
from time import sleep, ctime

# 创建 Thread 的子类
class MyThread(Thread):
    def __init__(self, func, args):
        '''
        :param func: 可调用的对象
        :param args: 可调用对象的参数
        '''
        Thread.__init__(self)
        self.func = func
        self.args = args
        self.result = None

    def run(self):
        self.result = self.func(*self.args)

    def getResult(self):
        return self.result


def func(name, sec):
    print('---开始---', name, '时间', ctime())
    sleep(sec)
    print('***结束***', name, '时间', ctime())
    return sec


def main():
    # 创建 Thread 实例
    t1 = MyThread(func, (1, 1))
    t2 = MyThread(func, (2, 2))
    # 启动线程运行
    t1.start()
    t2.start()
    # 等待所有线程执行完毕
    t1.join()
    t2.join()
    # 或线程中程序的运行结果
    print(t1.getResult())
    print(t2.getResult())


if __name__ == '__main__':
    main()
```

## 多线程的同步

https://zhuanlan.zhihu.com/p/94344847

多个线程共享一个进程的资源和地址空间，难免会有竞争

### 锁机制

#### 互斥锁

```python
import threading
import time
lock=threading.Lock()
num=9
def func():
    global num  # 全局变量
    lock.acquire()  # 获得锁，加锁
    num1 = num
    time.sleep(0.1)
    num = num1 - 1
    lock.release()  # 释放锁，解锁
    time.sleep(2)
l=[]
for i in range(10):  # 开启100个线程
    t = threading.Thread(target=func, args=())
    t.start()
    l.append(t)

# 等待线程运行结束
for i in l:
    i.join()
print(num)
```

这边加了锁得出-1，而没有锁就是8，为什么？

这里就牵扯到GIL了，因为Python的多线程虽说是多线程，但是在同一时刻还是只能有一个线程占用解释器，所以如果没有锁，那么在第一个线程执行到第一个sleep的时候，就会做一次调度让给下一个线程执行，此时num还没有重新赋值。但是如果加了锁，那么在在执行到sleep后即使做了调度，那么由于处于临界区，导致无法继续进行。

#### 死锁出现

四个条件：

1. 互斥。资源只能被一个线程拥有
2. 占用等待。线程已经获取了一部分资源并等待获取剩下资源
3. 不可抢占。线程不可被其他线程强行终止。
4. 环路等待。线程需要的资源被其他线程占据并形成环路。

#### 递归锁

也叫可重入锁，为了支持同一个线程中多次请求同一资源，Python 提供了可重入锁(RLock)。这个RLock内部维护着一个锁(Lock)和一个计数器(counter)变量，counter 记录了acquire 的次数，从而使得资源可以被多次acquire。直到一个线程所有 acquire都被release(计数器counter变为0)，其他的线程才能获得资源。

如果是在一个递归函数中，那么可重入锁就会变得很有用。

```python
import time
import threading

# 生成一个递归对象
Rlock = threading.RLock()


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self) -> None:
        self.fun_A()
        self.fun_B()

    def fun_A(self):
        Rlock.acquire()
        print('A加锁1', end='\t')
        Rlock.acquire()
        print('A加锁2', end='\t')
        time.sleep(0.2)
        Rlock.release()
        print('A释放1', end='\t')
        Rlock.release()
        print('A释放2')

    def fun_B(self):
        Rlock.acquire()
        print('B加锁1', end='\t')
        Rlock.acquire()
        print('B加锁2', end='\t')
        time.sleep(3)
        Rlock.release()
        print('B释放1', end='\t')
        Rlock.release()
        print('B释放2')


if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread()
    t1.start()
    t2.start()
```

执行过程：

```
A加锁1  A加锁2  A释放1  A释放2
A加锁1  A加锁2  A释放1  A释放2
B加锁1  B加锁2  B释放1  B释放2
B加锁1  B加锁2  B释放1  B释放2
```

虽然A遇到了sleep，但是没有做线程的切换

### 信号量

```python
import threading
import time,random
sem=threading.Semaphore(3) #规定了只有三个线程可以

def func():
    if sem.acquire():
        print(threading.current_thread().getName()+"GET")
        time.sleep(random.randint(1,5))
        sem.release()

for i in range(10):
    thread=threading.Thread(target=func,args=())
    thread.start()
```

这样可以保证只有三个线程可以占用资源，如果设为1的话，那就是互斥型信号量了。

### Condition

条件通知，当一个线程完成指定任务后通知其他线程可以执行

#### 例一

生产者生产成功后通知消费者消费，消费者消费完后通知生产者生产

```python
import threading
import time

product=None
condition=threading.Condition()

def producer():
    global product
    if condition.acquire():
        while True:
            print("__Start__")
            if not product:
                product="鞋子"
                print('---生产产品:%s---' % product)
                condition.notify()
            condition.wait()
            time.sleep(2)

def consumer():
    global product
    if condition.acquire():
        while True:
            print('***执行，consume***')
            if product is not None:
                print('***卖出产品:%s***' % product)
                product = None
                # 通知生产者，商品已经没了
                condition.notify()
            # 等待通知
            condition.wait()
            time.sleep(2)

if __name__=='__main__':
    t1 = threading.Thread(target=consumer)
    t1.start()
    t2 = threading.Thread(target=producer)
    t2.start()
```

**acquire()** 获得锁(线程锁)
**release()** 释放锁
**wait(timeout)** 挂起线程timeout秒(为None时时间无限)，直到收到notify通知或者超时才会被唤醒继续运行。必须在获得Lock下运行。
**notify(n=1)** 通知挂起的线程开始运行，默认通知正在等待该condition的线程，可同时唤醒n个。必须在获得Lock下运行。
**notifyAll()** 通知所有被挂起的线程开始运行。必须在获得Lock下运行。

### Event事件

```python
import threading

event = threading.Event()


def func():
    print('等待服务响应...')
    print(event.is_set())
    event.wait()  # 等待事件发生
    print(event.is_set())
    print('连接到服务')


def connect():
    print('成功启动服务')
    event.set()


t1 = threading.Thread(target=func, args=())
t2 = threading.Thread(target=connect, args=())

t1.start()
t2.start()
```

打印结果

```shell
等待服务响应...
False
成功启动服务
True
连接到服务
```

**wait(timeout=None)** 挂起线程timeout秒(None时间无限)，直到超时或收到event()信号开关为True时才唤醒程序。
**set()** Even状态值设为True
**clear()** Even状态值设为 False
**isSet()** 返回Even对象的状态值。

