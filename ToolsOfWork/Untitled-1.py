# import os
# file=os.listdir('E:\\temp\\')
# for i in file:
#     if 'csv' in i: 
#         f=open('e:\\temp\\'+i,'r',encoding='utf-8')
#         k=f.readlines()

f=open('e:\\temp\\1108LTE关键指标.csv','rb')
for i in f.readlines():
    print(i.decode('utf-8','ignore'))

        