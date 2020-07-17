import os
path='E:\\temp\\投诉\\数据\\'

bad_cell_shutdown={}
bad_cell_fault={}

f=open(path+'cell.csv')
for line in f.readlines():
    line=line.replace('\n','')
    bad_cell_shutdown[line]={}
    bad_cell_fault[line]={}
f.close()

f=open(path+'LTErelations.csv','r')
for line in f.readlines():
    line=line.replace('\n','').split(',')
    if line[0] in bad_cell_fault:
        bad_cell_fault[line[0]][line[1]]=''
        bad_cell_fault[line[0]][line[3]]=''
        bad_cell_shutdown[line[0]][line[0]]=''
        bad_cell_shutdown[line[0]][line[2]]=''        
f.close()
print(bad_cell_fault,bad_cell_shutdown)
for i,j in bad_cell_fault.items():
    for k in j:
        print(k)


# for file in os.listdir:
#     if '告警' in file:
#         f=open(path+file,'r',encoding='utf-8')
#         f

