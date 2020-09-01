# from threading import Thread
# def func(name):
#     print(f"name:{name}")

# thread1=Thread(target=func,args=("mason",))
# thread2=Thread(target=func,args=("Juli",))
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()

# from threading import Thread
# from time import sleep, ctime


# class MyClass(object):

#     def func(self,name,sec):
#         print('---开始---', name, '时间', ctime())
#         sleep(sec)
#         print('***结束***', name, '时间', ctime())

# def main():
#     # 创建 Thread 实例
#     t1 = Thread(target=MyClass().func, args=(1, 1))
#     t2 = Thread(target=MyClass().func, args=(2, 2))

#     # 启动线程运行
#     t1.start()
#     t2.start()

#     # 等待所有线程执行完毕
#     t1.join()  # join() 等待线程终止，要不然一直挂起
#     t2.join()

# if __name__=="__main__":
#     main()

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