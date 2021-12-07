# 일반함수로 쓰레드 만드는 방법

import time
from threading import Thread
def genFn():
    for n in range(11,20):
        print('n=',n)
        time.sleep(1)

def thFn(a,b):
    print( a, b)
    for n in range(10):
        print('n=',n)
        time.sleep(1)

genFn()
# thFn()
t = Thread( target=thFn ,args=('hello','thread') ) # 쓰레드함수..
t.start()
print('hello')