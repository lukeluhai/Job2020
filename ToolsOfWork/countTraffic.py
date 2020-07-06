import os
a=os.listdir('E:\\temp\\traffic\\1\\')
print(a)
countGSMErl={}
countGSMGB={}
countGSMNo={}

countLTEErl={}
countLTEGB={}
countLTENo={}




for i in a:
    f=open('E:\\temp\\traffic\\1\\'+i)
    for j in f.readlines():
        b=j.split('|')
        if b[2]=="LTE":
            if b[0] in countLTEErl:
                countLTEErl[b[0]]+=float(b[5])
                countLTEGB[b[0]]+=float(b[6])
                countLTENo[b[0]]+=1
            else:
                countLTEErl[b[0]]=float(b[5])
                countLTEGB[b[0]]=float(b[6])
                countLTENo[b[0]]=1
        if b[2]=="GSM":
            if b[0] in countGSMErl:
                countGSMErl[b[0]]+=float(b[5])
                countGSMGB[b[0]]+=float(b[6])
                countGSMNo[b[0]]+=1
            else:
                countGSMErl[b[0]]=float(b[5])
                countGSMGB[b[0]]=float(b[6])
                countGSMNo[b[0]]=1
    f.close


    print(countLTEGB)
    print(countLTEErl)
    print(countLTENo)


    print(countGSMGB)
    print(countGSMErl)
    print(list(countGSMNo.keys()))


lteKey=countLTENo.keys()
for i in lteKey:
    print(str(i)+"|"+str(countLTEErl[i])+"|"+str(countLTEGB[i])+"|"+str(countLTENo[i])+"|GSM|"+str(i)+"|"+str(countGSMErl[i])+"|"+str(countGSMGB[i])+"|"+str(countGSMNo[i]))

