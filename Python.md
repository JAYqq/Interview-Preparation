## python切片细节

https://www.jianshu.com/p/15715d6f4dad

```csharp
object[start_index:end_index:step] 
```

**很重要记住step>0就是从左往右**

- a[-1]是最后一个，所以a[-2]是倒数第2个
- 切取完整的对象a[:]
- a[::]从左往右，arr[::,-1]从右往左
- a[:6:-1]从右往左直到第6个结束如果a从0~9，那么这个就是9,8,7
- a[6::-1]  从第六个位置开始，从右往左取值
- a[:-6:-1]   从终点开始，从右往左，直到第六个（不包括，相当于右开，所以也相当于取5个值）：[9,8,7,6,5]
- **多层切片操作**                   a[:8] [2:5] [-1:]，可以一层一层分开来计算
- 在某个位置插入元素，比如arr=[1,2,3]，那么arr[1:1]=[9]，那么就会变成arr[1,9,2,3]，插入只能是可迭代对象

**原理**

https://zhuanlan.zhihu.com/p/79752359

1. python的可迭代对象比如集合[]，做切片操作[1:2]，就会调用___getitem___()方法：

   ```python
    class A():
        def __getitem__(self, key):
            print('__getitem__ is called')
            print('key={}'.format(key))
        def __setitem__(self, key, val):
            print('__setitem__ is called')
            print('key={}, val={}'.format(key, val))
   ```

   做切片的时候这个key值就是一个slice函数

   ```python
    >>> mySlice[0:3]
    __getitem__ is called
    key=slice(0, 3, None)
    >>> mySlice[:5]
    __getitem__ is called
    key=slice(None, 5, None)
    >>> mySlice[:100:5]
    __getitem__ is called
    key=slice(None, 100, 5)
   ```

   所以上面说的start、end、step都是slice函数的参数，默认值是None。

   **slice**

   `slice`类只有四个成员，其中`start`, `stop`, `step`是成员变量，`indices`类是成员函数。

   这个indices是这么用的：

   ```python
   >>> a = slice(5, 10, 2)
    >>> b = a.indices(20)
    >>> b
    (5, 10, 2)
    >>> list(range(*b))
    [5, 7, 9]
   ```

   a只是一个元祖，没有任何意义，当a调用了indices方法，传入一个length值，那么这个元祖就是为这个length服务了.所以range函数可以配合上这个元祖，返回长为20的数组进行这些切片操作得出来的值的真正索引

   

## 手写一个打印程序运行时间的装饰器

```python
import time
def gettime(func):
    def inner(*args,**kwargs):
        start_time=time.time()
        time.sleep(2)
        func(*args,**kwargs)
        dur=time.time()-start_time
        print(dur)
    return inner

@gettime
def main():
    sum=1
    for i in range(1000):
        sum+=1
main()
```

如果装饰器需要接受参数，那么需要在原来的基础上再增加一层，见自己的另一篇。

如果需要拿到原函数的返回值，那么就要在装饰器中调用原函数时接受返回值。

**装饰器的原理**

实现一个闭包，闭包就是将函数作为一个返回值传递给对象，它可以将本地变量脱离它的作用域而存在。通过@这个语法糖将函数作为参数传递到装饰器，装饰器内部去调用这个函数。



## Python中的多继承

每个类都有一个属性/      (__mro__)它的值是一个元祖，里面记录了当前类的方法解析顺序，知道object。

class A(B,C)   如果B和C中都有一个相同的方法，那么在A中调用这个方法只会调用B的，因为在mro元祖中B的顺序在C之前。如果需要调用C，那么需要显示调用C.test(self)



## GIL全局解释器锁。

这个只有在Cpython解释器中才有，因为Cpython不是线程安全的，因为Cpython使用的是系统原生的线程，在Linux的pthread完全由操作系统调度执行。pthread本身不是线程安全的，需要使用者通过锁来实现多线程的安全运行，因此CPython解释器下的Python实现多线程也必然存在线程不安全的问题。所以在解释器层面实现了一把全局互斥锁，来保护Python对象从而实现对单核CPU的使用率

https://zhuanlan.zhihu.com/p/87307313

### **GIL隐患**

- 在多核CPU的主机上，由于存在GIL导致无论有多少线程开启，同一时刻只有一个线程在执行，这导致了在多核CPU情况下，效率还不如单线程执行效率高
- 对于CPU密集型的计算类程序GIL就有比较大的问题，因为CPU密集型的程序本身没有太多等待，不需要解释器介入并且所有任务只能等待1个核心，其他核心空闲也无法使用，这么看对多核的使用确实很糟糕。

### **优势**

- 在单核CPU上执行多线程可以由解释器实现有效的调度。在IO密集型程序上，GIL的存在也不会让效率很低下

### **GIL缺陷的解决方案**

python作为生命力极强的热门语言，绝对不会在多核时代坐以待毙。即便有GIL的限制，仍然有许多方法让程序拥抱多核。

- **多进程**:Python2.6引入了MultiProcess库来弥补Threading库中GIL带来的缺陷，基于此开发多进程程序，每个进程有单独的GIL,避免多进程之间对GIL的竞争，从而实现多核的利用，但是也带来一些同步和通信问题，这也是必然会出现的。
- **Ctypes**:CPython的优势就是与C模块的结合，因此可以借助Ctypes调用C的动态库来实现将计算转移，C动态库没有GIL可以实现对多核的利用。（也就是python去调用C，实现多核利用）
- **协程**:协程也是一个很好的手段，在Python3.4之前，官方没有对协程的支持，存在一些三方库的实现，比如gevent和Tornado。3.4之后就内置了asyncio标准库，官方真正实现了协程这一特性。

GIL问题的并不是编程语言的本身问题，换做其他语言只是将问题转移到了用户层面，需要用户自己实现线程安全。

## Python如何判断变量的类型

- isinstance
- type

### **区别**

是否考虑继承关系

- isinstance() 会认为子类是一种父类类型，考虑继承关系。Class A(B)  认为A就是B
- type() 不会认为子类是一种父类类型，不考虑继承关系。相反

## 元类 type

实例是由类创建的，而类是由元类创建的。也就是元类创建的对象叫做类，类创建实例

```python
def func(self):
    print("do sth")

Klass = type("Klass", (), {"func": func})

c = Klass()
c.func()
```

这样来创建一个类

## `*args` and `**kwargs`

一个星（*）：表示接收的参数作为元组来处理

两个星（**）：表示接收的参数作为字典来处理

## xrange和range区别

- Xrange生成的是一个生成器，而range是直接开辟了一个List，但是Python3已经取消了xrange
- Xrange在生成很大序列的时候性能更好

## Python中的dict实现

内部是一个哈希表，处理哈希冲突的时候是采用了开放寻址的方法。当出现哈希冲突的时候，利用探测函数往后找到一个空的位置插入。

## @staticmethod 和@classmethod

类方法接受的第一个参数是cls，这个的意思是接受类作为参数，而不是实例，所以不同实例如果通过调用一个类方法进行成员变量的修改，那么修改的是一个变量。而staticmethod不接受self、cls，只能通过A.method或者a.method调用，而不能在类内部使用self.method调用，因为它的生命周期已经脱离类了。

## Python实现单例模式

### 利用__new__

```python
class Single(object):
    __instance=None
    def __new__(cls,*args,**kargs):
        if not cls.__instance:
            cls.__instance=object.__new__(cls,*args,**kargs)
        return cls.__instance
    def __init__(self):
        pass

s=Single()
s2=Single()
print(id(s),id(s2)) #一样的
```

这里通过一个instance是否是None来决定是否返回

### 利用元类

```python
class Singleton(type):
    __instances={}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls]=super(Singleton,cls).__call__(*args,**kwargs)
        return cls.__instances[cls]

class Sin2(metaclass=Singleton):
    pass

cls1 = Sin2()
cls2 = Sin2()
print(id(cls1) == id(cls2))
```

首先要知道如何使用type创建一个类（上面有）

直接继承自type表示这是一个元类。

我们创建实例的时候，会主动去调用元类的call，其实是括号的作用，**因为Python中一切都是对象，对象分为可调用和不可调用，他们的区别就是是否有call方法可以调用**，比如一个类A，我们如果可以A( )这样表示它是可调用的

```python
class A:
  pass
a=A()  #A可调用
a(1,2)  #a可调用
```

所以这里 super(Singleton,cls) 表示 t=type()，然后调用call表示a(1,3)，也就是赋值传参。

### 利用装饰器

```python
class Singleton:
    def __init__(self,cls):
        self.__cls=cls
        self.__instances={}
    
    def __call__(self):
        if self.__cls not in self.__instances:
            self.__instances[self.__cls]=self.__cls()
        return self.__instances[self.__cls]
@Singleton
class Sin2:
    def __init__(self):
        pass

s1=Sin2()
s2=Sin2()
print(id(s1)==id(s2))
```

这边是类装饰器，把类作为参数传递进去来做制约实例化操作。

**其实我们要实现单例模式其实就是制约这个类只能被创建一个实例，那么我们自然而然就能想到在类创建实例之前做点制约条件就可以，像是一个魔性的互斥锁。**

## Python中的描述符类

### 一般类的对象访问

首先我们要弄清楚对于一个用户自定义的类，我们访问其成员的内部流程，比如现在我们有这样一个类：

```python
class Afnper(object):
    def __init__(self,name):
        self.name=name
a=Afnper("mason")
```

然后我们查看一下这个类的具体信息

```shell
>>> dir(Afnper)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```

我们主要关注两个，一个是dict，还有一个是getattribute，当我们访问name这个成员的时候：

```shell
>>> a.__dict__   #首先是从实例a的__dict__中寻找，这里是找到了所以不会继续往下
{'name': 'mason'}
>>> dir(Afnper)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>> a.__dict__['name']  #如果没找到的话，那么就会到实例所属的类找
'mason'
>>> type(a).__dict__['name']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'name'
#后面要是还没找到，可能就会从基类去找
```

**但是，如果type(a)是一个描述符类，那么就会改变这个寻找的规律**

那么什么是描述符类？

### 描述符类

#### 定义

- 一个描述符是一个有“绑定行为”的对象属性(object attribute)，它的访问控制会被描述器协议方法重写。
- 任何定义了 `__get__`, `__set__` 或者 `__delete__` 任一方法的类称为描述符类，其实例对象便是一个描述符，这些方法称为描述符协议。
- 当对一个实例属性进行访问时，Python 会按 `obj.__dict__` → `type(obj).__dict__` → `type(obj)的父类.__dict__` 顺序进行查找，如果查找到目标属性并发现是一个描述符，Python 会调用描述符协议（也就是描述符类定义访问属性的方法）来改变默认的控制行为。
- 描述符是 `@property``@classmethod``@staticmethod` 和 `super` 的底层实现机制。

那么我们知道了，只要一个类中定义了`__get__`, `__set__` 或者 `__delete__`其中的一个，这个类就叫做描述符类（描述器）

#### 特性

- 同时定义了 `__get__` 和 `__set__` 的描述符称为 数据描述符(data descriptor)；仅定义了 `__get__ `的称为 非数据描述符(non-data descriptor) 。两者区别在于：如果 `obj.__dict__` 中有与描述符同名的属性，若描述符是数据描述符，则优先调用描述符，若是非数据描述符，则优先使用 `obj.__dict__` 中属性。
- 描述符协议必须定义在类的层次上，否则无法被自动调用。

#### 举栗子

```python
class ReadonlyNumber(object):
    """
    实现只读属性(实例属性初始化后无法被修改)
    利用了 data descriptor 优先级高于 obj.__dict__ 的特性
    当试图对属性赋值时，总会先调用 __set__ 方法从而抛出异常
    """
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        raise AttributeError(
            "'%s' is not modifiable" % self.value
         )

class Circle(object):

    pi = ReadonlyNumber(3.14)

    def __init__(self, radius):
        self.radius = radius

    @LazyProperty
    def area(self):
        print('Computing area')
        return self.pi * self.radius ** 2
```

首先清楚这边的ReadonlyNumber由于实现了get和set两个方法，所以这已经是一个描述符类了。当我们在Circle类中创建了pi后，**我们调用self.pi会发生什么？**

这个问题解决了，描述符也就弄清楚了。

其实这里十分巧妙的使用了数据描述符的优先级会比`__dict__`的优先级要高，所以会直接调用`__get__`方法去返回一个值，而不是去寻找dict中的值。**但是，是怎么实现这个优先级的呢？**。

其实在调用`__get__`之前，是先调用`__getattribute__`方法的，这个方法内部实现了优先级的判定，**其实优先级的判定也就是判断是否有`__get__方法在`**，所以它的实现是这样的：

```python
def __getattribute__(self, key):
    "Emulate type_getattro() in Objects/typeobject.c"
    v = object.__getattribute__(self, key)
    if hasattr(v, '__get__'):
       return v.__get__(None, self)
    return v
```

而__getattribute__方法其实就是相当于object.`__dict__`.get(attr,None)

所以，对于一个实现了`__get__`的数据描述符类来说，其实self.pi就变成了type(self).__dict__['x'].__get__(self, type(self))，如下：

```shell
>>> class Test(object):
...    value=ReadonlyNumber(3.14)
...
>>> t=Test()
>>> dir(t)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'value']
>>> t.__dict__
{}
>>> Test.__dict__
mappingproxy({'__module__': '__main__', 'value': <__main__.ReadonlyNumber object at 0x10e50f5b0>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None})
>>> Test.__dict__['value']
<__main__.ReadonlyNumber object at 0x10e50f5b0>
>>> type(t).__dict__['value'].__get__(t,type(t))  #对于t.value就通过getattribute就变成了这样
3.14
```

ok清楚了。

### 常见的例子

比如Python的@property属性，就是利用了描述符类

```python
class Decorator(object):
 
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc
 
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.fget(instance)
 
    def __set__(self, instance, value):
        self.fset(instance, value)
 
    def __delete__(self, instance):
        self.fdel(instance)
 
    def getter(self, fget):
        return Decorator(fget, self.fset, self.fdel, self.__doc__)
 
    def setter(self, fset):
        return Decorator(self.fget, fset, self.fdel, self.__doc__)
 
    def deleter(self, fdel):
        return Decorator(self.fget, self.fset, fdel, self.__doc__)
 
 
class Target(object):
    desc = "Amazing pyhton"
 
    def __init__(self, attr=5):
        self._x = attr
    @Decorator
    def show(self):  #这样，调用self.show的时候就跟上面self.pi一样通过getattribute调用了__get__方法了
        return self._x
 
    @show.setter
    def show(self, value):
        self._x = value
 
    @show.deleter
    def show(self):
        del self._x
```

