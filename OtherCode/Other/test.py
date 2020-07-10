
import os
fpath=os.listdir(r'E:\temp\DT20200512172735')
print(fpath)

for i in fpath:
    f=open('E:\\temp\\DT20200512172735\\'+i)
    a=[]
    for line in f.readlines():
        if line not in a:
            a.append(line)
    f.close
    g=open('E:\\temp\\DT20200512172735\\_'+i,'w')
    g.writelines(a)
    g.close()

