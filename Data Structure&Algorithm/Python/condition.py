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
