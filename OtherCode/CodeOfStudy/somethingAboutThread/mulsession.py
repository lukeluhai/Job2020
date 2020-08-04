from threading import Thread
from multiprocessing import Process
import os
import time
def work():
    print('hello')

if __name__ == '__main__':
    s1 = time.time()
    #在主进程下开启线程
    t=Thread(target=work)
    t.start()
    t.join()
    t1 = time.time() - s1
    print('进程的执行时间：',t1)
    print('主线程/主进程')
    '''
    打印结果:
    hello
    进程的执行时间： 0.0
    主线程/主进程
    '''

    s2 = time.time()
    #在主进程下开启子进程
    t=Process(target=work)
    t.start()
    t.join()
    t2 = time.time() - s2
    print('线程的执行时间：', t2)
    print('主线程/主进程')
    '''
    打印结果:
    hello
    线程的执行时间： 0.5216977596282959
    主线程/主进程
    '''
