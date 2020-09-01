import threading
import time,random
sem=threading.Semaphore(3)

def func():
    if sem.acquire():
        print(threading.current_thread().getName()+"GET")
        time.sleep(random.randint(1,10))
        sem.release()

for i in range(10):
    thread=threading.Thread(target=func,args=())
    thread.start()