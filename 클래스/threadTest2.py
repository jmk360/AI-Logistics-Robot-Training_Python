# 클래스 기반 쓰레드 생성하는 방법

from threading import Thread
import time
class MyThread(Thread): #상속
    def __init__(self):
        super().__init__() #상위생성자호출

    def run(self): #재정의
        for n in range(1,10):
            print('n=',n)
            time.sleep(1)

th = MyThread()
th.start()
print('hello')
for n in range(11,20):
    print("n=",n)
    time.sleep(1)