import os

f=open('E:\\KanKan\\VaCache\\aa.txt','w',encoding='utf-8')

def printFile(path,name):
    if os.path.isfile(path+'\\'+name):
        f.writelines(name+'||'+path+'\n')

    else:
        for i in os.listdir(path+'\\'+name):
            printFile(path+'\\'+name,i)
    return
printFile(r'E:\KanKan\VaCache\movie','潘多拉')
f.close()
