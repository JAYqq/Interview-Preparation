## python中的装饰器

Python中的装饰器其实也是一种函数， 它可以在不修改原函数代码情况下扩展原函数功能。装饰器函数与普通函数不同之处就在于装饰器函数返回了一个函数对象，装饰器利用了闭包的原理来实现。主要用于日志插入，权限管理等等。

```python
import logging
def log(func):
    def code(*args,**kwargs): 
        #print("log :",func.__name__)
        logging.warning(func.__name__)
        return func(*args,**kwargs)
    return code

@log
def run(a,b):
    print("a+b",a+b)


if __name__=="__main__":
    run(2,3)
```

这里使用了一个基本的装饰器构造（不带参数），打印结果为：

```python
WARNING:root:run
a+b 5
```

如果**有带参数**的话，就可以：

```python
import logging

def log(level):
    def decorator(func):
        def code(*args, **kwargs):
            logging.warning(level)
            return func(*args, **kwargs)
        return code
    return decorator


@log(level="warning")
def run(a, b):
    print("a+b", a+b)


if __name__ == "__main__":
    run(2, 3)

```

打印出：

```python
WARNING:root:warning
a+b 5
```

上面的装饰器实际上是一个含参数的闭包环境，将装饰器包裹起来，并返回一个装饰器

### 类装饰器

```python
import logging
class log(object):
    def __init__(self,func):
        self._func=func
    def __call__(self):
        print("class log running",self._func.__name__)
        self._func()
        print("class log ending",self._func.__name__)


@log
def run():
    print("run")

if __name__ == "__main__":
    run()
```

类装饰器相比一般的装饰器具有灵活度大、高内聚、封装性的特点，主要就是利用了函数___call___来，装饰器被装饰到函数上后就会调用这个call函数

### **functools.wraps**

如果我们是这样的一个装饰器：

```python
def log(func):
    @wraps(func)
    def code(*args,**kwargs): 
        """code run"""
        print("log :",func.__name__)
        return func(*args,**kwargs)
    return code

@log
def run(a,b):
    """hello world"""
    #print("a+b",a+b)
    return a+b


if __name__=="__main__":
    run(2,3)
    print(run.__name__)
    print(run.__doc__)
```

那么我们会发现，我们run函数的元信息就变成了：

```python
log : run
code
code run
```

这样run函数的信息就被修改了，这是不符合我们的互不影响原则的，所以这时候就需要functools.wraps装饰器

```python

import logging
from functools import wraps
def log(func):
   # @wraps(func)
    def code(*args,**kwargs): 
        """code run"""
        print("log :",func.__name__)
        return func(*args,**kwargs)
    return code

@log
def run(a,b):
    """hello world"""
    #print("a+b",a+b)
    return a+b


if __name__=="__main__":
    run(2,3)
    print(run.__name__)
    print(run.__doc__)
```

这时候就变成了：

```python
log : run
run
hello world
```

### 内置装饰器

1. 静态方法@staticmethod

   这是一个可以直接把用类名调用的函数，不需要实例化以后再调用

   ```python
   
   class Myclass:
       num=2
       
       def fun(self):
           print("no decorate")
   
       @staticmethod
       def my_static_method():
           print('This is a static method')
   
       @classmethod
       def my_class_method(cls,sth):
           print('This is a class method of', cls.a,sth)
   ```

   我们可以直接Myclass.my_static_method访问，但是它的前提就是它装饰的函数一般不加self和其他参数了，**所以它的应用场景一般只用来return或者print一些数据就可以了**。

2. 类方法@classmethod

   这个装饰器其实跟上面的staticmethod差不多，但是它主要用在带参数的方法，也是对staticmethod的一种拓展。他们两种都是不需要实例化访问的，**有利于组织代码和命名空间的整洁**

3. 类属性@property

   这个属性简单来讲就是可以把一个函数当作属性来访问。比如现在我们有一个需求，就是需要计算出长方形的面积和周长，并且可以访问到它的长宽。但是我们的长宽虽然可以直接self.width和self.height访问到，但是面积和周长需要计算，所以我们只能这样访问到，self.area(self.width,self,height)，但是这不符合我们的规范。这时候我们就可以这样来定义这个类：

   ```python
   class Rectangle(object):
       def __init__ (self,width,height):
           self.__width = width
           self.__height = height
   
       @property
       def width(self):
           return self.__width
       
       @width.setter
       def width(self, size):
           self.__width= size
       
       @property
       def height(self):
           return self.__height
       
       @height.setter
       def height(self,size):
           self.__height=size
   
       @property
       def area(self):
           return self.width*self.height
       
       @property
       def perimeter(self):
           return (self.width+self.height)*2
   re=Rectangle(10,20)
   print(re.area)#200
   print(re.perimeter)#60
   ```

   

注意到这里需要再设置两个:@height.setter和@width.setter

总之，python中的装饰器应用场景非常广，但是也很少有人讲清楚，这里也知识浅析没有深入了解