import os
path='E:\\temp\\投诉\\0629规划数据\\0629规划数据\\'
cgipath='E:\\temp\\基础信息\\LTE轩池基础信息表0714\\cgi.csv'
cell={}
f=open(cgipath,'r')
for line in f.readlines():
    a=line.replace('\n','').split(',')
    cell[a[0]]=a[1]+','+a[2]
f.close()
files=os.listdir(path)
relations=[]
for file in files:
    f=open(path+file,'r',encoding='utf-8')
    for line in f.readlines():
        if '460' not in line:
            continue
        celln=line.replace('\n','').split(',')
        if (('460-00-'+celln[7]+'-'+celln[6]) in cell) and ('460-00-'+celln[10]+'-'+celln[11]) in cell:
            relations.append(cell['460-00-'+celln[7]+'-'+celln[6]]+','+cell['460-00-'+celln[10]+'-'+celln[11]]+'\n')
    f.close()
f=open(path+'LTErelations.csv','a')
f.writelines(relations)
f.close()

