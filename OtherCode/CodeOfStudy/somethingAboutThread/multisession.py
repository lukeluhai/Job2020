from threading import Thread
from multiprocessing import Process
import os 
def work():
    print('hello',os.getpid()) 
if __name__ == '__main__':
    t1=Thread(target=work)
    t2=Thread(target=work)    
    t1.start()    
    t2.start()    
    print('主线程/主进程pid',os.getpid())     
    #part2:开多个进程,每个进程都有不同的pid    
    p1=Process(target=work)    
    p2=Process(target=work)    
    p1.start()    
    p2.start()    
    print('主线程/主进程pid',os.getpid())