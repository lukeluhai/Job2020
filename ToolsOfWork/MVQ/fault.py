cell={}
f=open('E:\\temp\\频发差小区\\MVQ\\CELL.csv','r')
for i in f.readlines():
    n=i.replace('\n','').split(',')
    cell[n[0]]=n[3]
f.close()
print(cell)

cell2={}
fault1={}
fault2={}
f=open('E:\\temp\\频发差小区\\MVQ\\附近小区集.csv','r')
for i in f.readlines():
    n=i.replace('\n','').split(',')
    if n[0] in cell and n[14]=='是':
        if n[0] not in cell2:
            cell2[n[0]]=[]
            fault1[n[6]]=""
            fault2[n[6]]=""
        else:
            cell2[n[0]].append(n[6])
            fault1[n[6]]=""
            fault2[n[6]]=""

f.close()
print(cell2)

f=open("E:\\temp\\频发差小区\\MVQ\\ALX告警.csv",'r')
for i in f.readlines():
    n=i.replace('\n','').split(',')
    if n[3] in fault1:
        if n[1]=='A2故障' or n[1]=='A3故障':
            fault1[n[3]]=[n[0],n[5]+' '+n[6]]
        if n[1]=='小区退服' or n[1]=='HALTED':
            fault2[n[3]]=[n[0],n[1]]
f.close()
# print(fault1)
# print(fault2)

f=open("E:\\temp\\频发差小区\\MVQ\\ZX告警.csv",'r')
for i in f.readlines():
    n=i.replace('\n','').split(',')
    if n[8] in fault1:
        if n[9]=='偶联断链' or n[9]=='以太网端口链路断':
            fault1[n[8]]=[n[6],n[9]]
        if n[9]=='小区中断告警' or n[9]=='站点ABIS控制链路断':
            fault2[n[8]]=[n[6],n[9]]            
f.close()
# print(fault1)
# print(fault2)

faultset={}
poweroffset={}

for x,y in cell2.items():
    for i in y:
        if i in fault1:
            if fault1[i]!="":
                faultset[x]=[i,fault1[i]]
        if i in fault2:
            if fault2[i]!="":
                poweroffset[x]=[i,fault2[i]]
                
print(faultset)
print(poweroffset)


g=open('E:\\temp\\频发差小区\\MVQ\\faultandoff.csv','w')
for x,y in cell.items():
    faultstr=',,'
    offstr=',,'
    if x in faultset:
        faultstr=faultset[x][0]+','+faultset[x][1][1]+','+faultset[x][1][0]
    if x in poweroffset:
        offstr=poweroffset[x][0]+','+poweroffset[x][1][1]+','+poweroffset[x][1][0]
    g.writelines(x+','+y+','+faultstr+','+offstr+'\n')
g.close()
#