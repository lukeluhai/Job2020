import os
import time
#print (time.strftime("%Y%m%d%H%M%S", time.localtime()) )

f=open('F:\\KanKan\\VaCache\\aa'+time.strftime("%Y%m%d%H%M%S", time.localtime())+'.csv','w',encoding='utf-8')

def printFile(path,name):
    if os.path.isfile(path+'\\'+name):
        f.writelines(name+'||'+path+'\n')

    else:
        for i in os.listdir(path+'\\'+name):
            printFile(path+'\\'+name,i)
    return
printFile(r'F:\\KanKan\\VaCache\\movie\\','潘多拉')
f.close()
