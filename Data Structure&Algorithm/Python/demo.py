class A(object):
    def foo(self,x):
        print("executing foo(%s,%s)"%(self,x))

    @classmethod
    def class_foo(cls,x):
        cls.num=x
        print("executing class_foo(%s,%s)"%(cls,cls.num))
    @classmethod
    def get_num(cls):
        print(cls.num)
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)"%x)
        
# class Single(object):
#     __instance=None
#     def __new__(cls,*args,**kargs):
#         if not cls.__instance:
#             cls.__instance=object.__new__(cls,*args,**kargs)
#         return cls.__instance
#     def __init__(self):
#         pass

# s=Single()
# s2=Single()
# print(id(s),id(s2))

# class Singleton(type):
#     __instances={}
#     def __call__(cls, *args, **kwargs):
#         print(cls)
#         if cls not in cls.__instances:
#             cls.__instances[cls]=super(Singleton,cls).__call__(*args,**kwargs)
#         return cls.__instances[cls]

# class Sin2(metaclass=Singleton):
#     pass

# cls1 = Sin2()
# cls2 = Sin2()
# print(id(cls1) == id(cls2))

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