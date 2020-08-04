import pandas as pd
import numpy as np
import os
import threading as thd
import time
path='D:\\快配表0727\\'
dframes=[]
isOver=0
t1=time.time()
print(t1)
def f_read_excel(path,filename):
    
    global isOver
    tt1=time.time()
    print('opening '+path,filename)
    b=pd.read_excel(path+filename,sheet_name='GGsmCell')
    # dframes.append(b)
    b.to_csv('d:\\'+filename)
    tt2=time.time()
    print(tt2-tt1)
    isOver+=1
# f_read_excel('ssssssssssssssssssss')

print('start at:',time.ctime())
threads=[]
for i in os.listdir(path):
    print(len(path+i))

    t=thd.Thread(target=f_read_excel,args=(path,i))
    # print(time.ctime())
    # print(i)
    # a=pd.read_excel(path+i,sheet_name=None)
    # c=a['GGsmCell']
    # dframes.append(c)
    threads.append(t)
for i in range(len(threads)):
    threads[i].start()
for t in threads:
    t.join()


result = pd.concat(dframes)
result.to_csv('d:\\GGsmCell2.csv')
print('end at:',time.ctime())
t2=time.time()
print(t2)
print(t2-t1)