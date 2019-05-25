## *args与**kwargs的区别

### *args

*args是是用来发送一个非键值对的可变数量的参数列表给一个函数，就像：

```python
>>> def test(args_f,*args_v):
...     print(args_f)
...     for x in args_v:
...             print(x)
...
>>> test('a','b','c','d')
a
b
c
d

```

### **kwargs

**kwargs允许我们将一个不定长度的键值对传给函数，就好像：

```python
>>> def demo(**kwargs):
...     for v,x in kwargs.items():
...             print(v,x)
...
>>> demo(name="mason",age="19")
name mason
age 19
```

我们也可以把一个已经存在的list,tuple和dict构造成*args 和 **kwargs传进函数里面，dict传入*args，list传到**kwargs这里有个例子：

```python
def demo(*args_f,**args_v):
   for x in args_f:
       print x        
   for k,v in args_v.items():
       print k+'='+v

list1 = [1,2,3]

dict = {'a':'A','b':'B','c':'C'}

demo(*list1,**dict)

## -- End pasted text --
1
2
3
a=A
c=C
b=B

```

前面我们明确指定了，*args 和 kwargs做为函数的参数，如果，我们没有指定*args 和 kwargs，我们定义的函数是这样的def demo(fargs,fargs1,fargs2): 我们怎么用*args 和 kwargs把参数传到函数里面？

我们就可以像下面这样：

```python
In [18]: %paste
list1 = [1,2,3]

dict = {'arg2':'A','arg1':'B','arg3':'C'}

def demo(arg1,arg2,arg3):
      print "arg1:", arg1
      print "arg2:", arg2
      print "arg3:", arg3

demo(*list1)
demo(**dict)

## -- End pasted text --
arg1: 1
arg2: 2
arg3: 3
arg1: B
arg2: A
arg3: C

```

这里我们的参数值跟传入的*args和**kwargs元素是一一对应的。