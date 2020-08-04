import pandas as pd
import numpy as np
import os
import threading as thd
import multiprocessing as p

import time


def f_read_excel(conn,path,filename):

    tt1=time.time()
    print('opening '+path,filename)
    b=pd.read_excel(path+filename,sheet_name='GGsmCell')
    # dframes.append(b)
    # b.to_csv('d:\\'+filename)
    tt2=time.time()
    print(tt2-tt1)
    conn.send(b)
    conn.close()
    print('end',os.getpid())

# f_read_excel('ssssssssssssssssssss')
if __name__=='__main__':
    path='D:\\快配表0727\\'
    dframes=[]

    t1=time.time()
    print(t1)


    print('start at:',time.ctime())
    threads=[]
    pips=[]

    for i in os.listdir(path):
    
        parent_conn,child_conn=p.Pipe()
        pips.append(parent_conn)
        t=p.Process(target=f_read_excel,args=(child_conn,path,i))
        # print(time.ctime())
        # print(i)
        # a=pd.read_excel(path+i,sheet_name=None)
        # c=a['GGsmCell']
        
        threads.append(t)
    for i in range(len(threads)):
        threads[i].start()

    for i in range(len(threads)):
        dframes.append(pips[i].recv())
        threads[i].join()


    result = pd.concat(dframes)
    result.to_csv('d:\\GGsmCell2.csv')
    print('end at:',time.ctime())
    t2=time.time()
    print(t2)
    print(t2-t1)