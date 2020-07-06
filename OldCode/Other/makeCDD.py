import os;
path = os.listdir('./cdd_log')
for logfileName in path:
    print (logfileName)
    f=open('D:\myproject\python\myproject\other\CDD_log\\'+logfileName,'r')
    lines=f.readlines()

    for i in range(0,len(lines)):
        print (lines[i])
        if 'Connected to ' in lines[i]:
            BSCName=lines[i].split(' ')[3]
            print(BSCName)
        if lines[i]=='CELL     CGI                  BSIC  BCCHNO  AGBLK  MFRMS  IRC':
            print(i)







