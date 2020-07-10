f=open('E:\\temp\\感知差小区\\工作簿1.csv','r')
a={}
for i in f.readlines():
    b=i.replace('\n','').split(',')
    a[b[0]]=b[1]
f.close()
result=[]
print(a)
g=open('E:\\temp\\感知差小区\\Allrelation.csv','r')
for i in g.readlines():
    c=i.replace('\n','').split(',')
    if c[0] in a:
        if c[1] in a:
            result.append(c[0]+','+a[c[0]]+','+c[1]+','+a[c[1]]+'\n')
            print(c[0]+','+a[c[0]]+','+c[1]+','+a[c[1]]+'\n')

g.close()

h=open('E:\\temp\\感知差小区\\Allrelation_.csv','a')
h.writelines(result)
h.close()

