import os
files=os.listdir('E:\\traffice\\1\\')
counts={}
for i in files:
    print(i)
    f=open('E:\\traffice\\1\\'+i)
    for line in f.readlines():
        if '|LTE|' in line:
            a=line.replace('\n','').split('|')
            if a[0] in counts:
                counts[a[0]]=counts[a[0]]+float(a[6])
                #counts[a[0]+'-'+a[1]]=counts[a[0]+'-'+a[1]]+1
            else:
                counts[a[0]]=float(a[6])
                print(a[0])
for key,value in counts.items():
    print(key,value)