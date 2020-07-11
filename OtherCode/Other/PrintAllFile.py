import os

f=open('F:\\1需要打印\\aa.txt','w',encoding='utf-8')

def printFile(path,name):
    if os.path.isfile(path+'\\'+name):
        f.writelines(name+'||'+path+'\n')

    else:
        for i in os.listdir(path+'\\'+name):
            printFile(path+'\\'+name,i)
    return
printFile(r'F:','1需要打印')
f.close()
