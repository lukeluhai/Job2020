path1='E:\\temp\\感知差小区\\cell2.csv'
path2='e:\\temp\\感知差小区\\RLNRP.CSV'
path3='e:\\temp\\感知差小区\\RLNRP_.CSV'
cell={}
cellrelation=[]
f=open(path1,'r')
for i in f.readlines():
    n=i.replace('\n','').split(',')
    cell[n[0]]=n[1]
f.close()

g=open(path2,'r')
for i in g.readlines():
    m=i.replace('\n','').split(',')
    if m[1] in cell:
        cellrelation.append(m[0]+','+m[1]+','+cell[m[1]]+'\n')
    else:
        cellrelation.append(m[0]+','+m[1]+','+   ''    +'\n')
g.close()

h=open(path3,'a')
h.writelines(cellrelation)
h.close()
