# import threading
# import time
# lock=threading.Lock()
# num=9
# def func():
#     global num  # 全局变量
#     lock.acquire()  # 获得锁，加锁
#     num1 = num
#     time.sleep(0.1)
#     num = num1 - 1
#     lock.release()  # 释放锁，解锁
#     time.sleep(2)
# l=[]
# for i in range(10):  # 开启100个线程
#     t = threading.Thread(target=func, args=())
#     t.start()
#     l.append(t)

# # 等待线程运行结束
# for i in l:
#     i.join()
# print(num)

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