import chardet
import os
defaultPath='E:\\temp\\基础信息\\查询表\\'
# 'E:\\temp\基础信息\\'
filePath=os.listdir(defaultPath)
while True:
    seekStr = input("请输入：")
    if seekStr=='exit':
            break
    else:
        a=os.system('cls')
        result=[]
        print('---------------------------------------------------------------')
        for dataFile in filePath:
            print(filePath)
            f=open(defaultPath+dataFile,'rb')
            #f.__next__()

            file_coding=chardet.detect(f.__next__())
            
            
            print(file_coding)
           

            if file_coding['encoding']=='GB2312':
                coding='gb18030'
            else:
                coding=file_coding['encoding']
            
            f.close()
            f=open(defaultPath+dataFile,'r',encoding=coding)
            #f=open('E:\\temp\\基础信息\\查询表\\'+dataFile,'r',encoding='utf-16')
            print(f.__next__())
            for line in f.readlines():
                if seekStr in line:
                    print(line)
            f.close()
        print(result)




