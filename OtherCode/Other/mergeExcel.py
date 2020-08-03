import pandas as pd
import numpy as np
import os
import threading as thd
import time
path='D:\\快配表0727\\'
dframes=[]
t1=time.time()


for i in os.listdir(path):
    
    print(i)
    tt1=time.time()
    a=pd.read_excel(path+i,sheet_name=None)
    c=a['GGsmCell']
    tt2=time.time()
    
    dframes.append(c)
    print(tt1-tt2)
result = pd.concat(dframes)
result.to_csv('d:\\GGsmCell.csv')
t2=time.time()
# print('time(sec):',)
print(t2-t1)
