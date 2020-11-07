import pandas as pd
import numpy as np
import os
import threading as thd
import multiprocessing as p

import time
def f_read_excel(conn,path,filename):

    tt1=time.time()
    print('opening '+path,filename)
    b=pd.read_excel(path+filename,sheet_name=None)
    # dframes.append(b)
    # b.to_csv('d:\\'+filename)
    tt2=time.time()
    print(tt2-tt1)
    conn.send(b)
    conn.close()
    print('end',os.getpid())


if __name__=='__main__':
    path='e:\\relation\\book\\'
    dframes=[]

 



    threads=[]
    pips=[]

    for i in os.listdir(path):
    
        parent_conn,child_conn=p.Pipe()
        pips.append(parent_conn)
        t=p.Process(target=f_read_excel,args=(child_conn,path,i))
        threads.append(t)
    
    for i in range(len(threads)):
        threads[i].start()

    for i in range(len(threads)):
        dframes.append(pips[i].recv())
        threads[i].join()
    sheets={}


    print('-------------------------------------')
    for book in dframes:
        for sheetname,sheetcontent in book.items():
            if sheetname in sheets:
                sheets[sheetname].append(sheetcontent)
            else:
                sheets[sheetname]=[sheetcontent]
    #print(sheets)
    writer = pd.ExcelWriter(path+'output.xlsx')
    for x,y in sheets.items():
        pd.concat(y).to_excel(writer,x,index=False)
    writer.save()


 
    # result = pd.concat(dframes)
    # result.to_csv('d:\\ExternalEUtranCellTDDLTE.csv',encoding='GBK')
    # print('end at:',time.ctime())
    # t2=time.time()
    # print(t2)
    # print(t2-t1)