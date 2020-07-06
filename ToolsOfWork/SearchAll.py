import os
defaultPath='E:\\temp\\traffic\\'
# 'E:\\temp\基础信息\\'
filePath=os.listdir(defaultPath)
while True:
    seekStr = input("请输入：")
    if seekStr=='exit':
            break
    else:
        a=os.system('cls')
        result=[]
        for dataFile in filePath:
            f=open(defaultPath+dataFile,'r',encoding='gbk')
            #f=open('E:\\temp\基础信息\\'+dataFile,'r',encoding='utf-16')
            print(f.__next__().split('\t'))
            for line in f.readlines():
                if seekStr in line:
                    print(line.split('\t'))
        print(result)




