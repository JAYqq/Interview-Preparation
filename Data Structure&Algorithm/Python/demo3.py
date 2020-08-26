class LazyProperty(object):
    """
    实现惰性求值(访问时才计算，并将值缓存)
    利用了 obj.__dict__ 优先级高于 non-data descriptor 的特性
    第一次调用 __get__ 以同名属性存于实例字典中，之后就不再调用 __get__
    """
    def __init__(self, fun):
        self.fun = fun

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.fun(instance)
        setattr(instance, self.fun.__name__, value)
        return value


class ReadonlyNumber(object):
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