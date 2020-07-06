f=open('E:\\temp\\d.txt','r')
for i in f.readlines():
    j=i.replace('\n','').split(',')
    if j[1]=="":
        continue
    a=len(j)
    #print(j)
    bb=map(lambda x:int(x),j[1:])
    #print(list(bb))
    b=map(lambda x:int(x)+1,j[1:])
    c=list(bb)+list(b)
    #print(c)
    d=len(set(c))
   # print(a,b)
    #print(d,a)
    if d!=(a-1)*2:
        print(j[0])