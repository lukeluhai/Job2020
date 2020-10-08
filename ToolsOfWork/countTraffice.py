import os
files=os.listdir('E:\\traffice\\')
counts={}
for i in files:
    f=open('E:\\traffice\\'+i)
    for line in f.readlines():
        if '|GSM|' in line:
            a=line.replace('\n','').split('|')
            if a[0]+'-'+a[1] in counts:
                counts[a[0]+'-'+a[1]]=counts[a[0]+'-'+a[1]]+float(a[6])
            else:
                counts[a[0]+'-'+a[1]]=float(a[6])
for key,value in counts.items():
    print(key,value)