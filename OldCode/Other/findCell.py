import os
import datetime


txtpath="H:\\temp\\ggggg\\"
filename=['a.txt']
findcell={}
c=open(txtpath+"cell.txt",'r')

for cell in c.readlines():
    findcell[cell.replace('\n','')]=1
c.close()
print(findcell)
result=[]
resultfile= open(txtpath+"result.csv", "w")
for i in filename:
    f=open(txtpath+i,'r')
    result.append(f.__next__())
    for r in f.readlines():
        if r.split(',')[0] in findcell:
            result.append(r)
    f.close()
resultfile.writelines(result)
resultfile.close()


