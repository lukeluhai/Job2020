def countif(a,b):
    n=0
    for i in a:
        if i!='':
            if float(i)>b:
                n+=1
    return n

            


CsvPath='D:\\temp\\人工评估\\csv\\'
f=open(CsvPath+'cell.csv','r')
Cell=f.readlines()
f.close
for i in range(len(Cell)):
    Cell[i]=Cell[i].replace('\n','').split(',')

DataDict={}
df=open(CsvPath+'msf.csv','r')
alllines=df.readlines()
alllines=list(set(alllines))

for line in alllines:
    tmpStr=line.replace('\n','').split(',')

    if tmpStr[8] in DataDict:
        DataDict[tmpStr[8]].append((tmpStr))
    else:
        DataDict[tmpStr[8]]=[(tmpStr)]







for CellLine in Cell:
    if CellLine[5] not in DataDict:
        continue

# TCH掉话率
    if CellLine[2]=='GSM TCH掉话' or CellLine[2]=='GSM简报T掉话' or CellLine[2]=='GSM简报T掉话':
        tmpStr=DataDict[CellLine[5]]
        tmpStr=sorted(tmpStr)
        if len(tmpStr)<7:
            continue

        tmpList=[]
        tmpList.append(tmpStr[0])
        tmpList.append(tmpStr[1])
        tmpList.append(tmpStr[2])
        tmpList.append(tmpStr[3])
        tmpList.append(tmpStr[4])
        tmpList.append(tmpStr[5])
        for i in range(6,len(tmpStr)):
            if len(tmpList)<7:
                tmpList.append(tmpStr[i])
            else:
                tmpList.pop(0)
                tmpList.append(tmpStr[i])
            n=0
            for x in tmpList:
                if float(x[24])<5:
                    n+=1
            
            if n>=5:
                f=open(CsvPath+'result.txt','a')
                f.writelines((CellLine[0]+"|"+CellLine[1]+"|"+"通过"
                    +"|"+"日期:"+tmpList[0][0]+",TCH掉话率（不含切换):"+tmpList[0][24]+'%'
                    +"|"+"日期:"+tmpList[1][0]+",TCH掉话率（不含切换):"+tmpList[1][24]+'%'
                    +"|"+"日期:"+tmpList[2][0]+",TCH掉话率（不含切换):"+tmpList[2][24]+'%'
                    +"|"+"日期:"+tmpList[3][0]+",TCH掉话率（不含切换):"+tmpList[3][24]+'%'
                    +"|"+"日期:"+tmpList[4][0]+",TCH掉话率（不含切换):"+tmpList[4][24]+'%'
                    +"|"+"日期:"+tmpList[5][0]+",TCH掉话率（不含切换):"+tmpList[5][24]+'%'
                    +"|"+"日期:"+tmpList[6][0]+",TCH掉话率（不含切换):"+tmpList[6][24]+'%\n'))
                f.close
                break
            
# SDCCH 建立成功率
    if CellLine[2]=='GSM SD建立成功率优化' or CellLine[2]=='GSM SD建立成功率' :
        tmpStr=DataDict[CellLine[5]]
        tmpStr=sorted(tmpStr)
        if len(tmpStr)<7:
            continue

        tmpList=[]
        tmpList.append(tmpStr[0])
        tmpList.append(tmpStr[1])
        tmpList.append(tmpStr[2])
        tmpList.append(tmpStr[3])
        tmpList.append(tmpStr[4])
        tmpList.append(tmpStr[5])
        for i in range(6,len(tmpStr)):
            if len(tmpList)<7:
                tmpList.append(tmpStr[i])
            else:
                tmpList.pop(0)
                tmpList.append(tmpStr[i])
            n=0
            for x in tmpList:
                if ( 0 if x[39]=='' else float(x[39]))>90:
                    n+=1
            
            if n>=7:
                f=open(CsvPath+'result.txt','a')
                f.writelines((CellLine[0]+"|"+CellLine[1]+"|"+"通过"
                    +"|"+"日期:"+tmpList[0][0]+",SDCCH建立成功率:"+tmpList[0][39]+'%'
                    +"|"+"日期:"+tmpList[1][0]+",SDCCH建立成功率:"+tmpList[1][39]+'%'
                    +"|"+"日期:"+tmpList[2][0]+",SDCCH建立成功率:"+tmpList[2][39]+'%'
                    +"|"+"日期:"+tmpList[3][0]+",SDCCH建立成功率:"+tmpList[3][39]+'%'
                    +"|"+"日期:"+tmpList[4][0]+",SDCCH建立成功率:"+tmpList[4][39]+'%'
                    +"|"+"日期:"+tmpList[5][0]+",SDCCH建立成功率:"+tmpList[5][39]+'%'
                    +"|"+"日期:"+tmpList[6][0]+",SDCCH建立成功率:"+tmpList[6][39]+'%\n'))
                f.close
                break

# GSM 无线接入性优化
    if CellLine[2]=='GSM 无线接入性优化'  :
        tmpStr=DataDict[CellLine[5]]
        tmpStr=sorted(tmpStr)
        if len(tmpStr)<7:
            continue

        tmpList=[]
        tmpList.append(tmpStr[0])
        tmpList.append(tmpStr[1])
        tmpList.append(tmpStr[2])
        tmpList.append(tmpStr[3])
        tmpList.append(tmpStr[4])
        tmpList.append(tmpStr[5])
        for i in range(6,len(tmpStr)):
            if len(tmpList)<7:
                tmpList.append(tmpStr[i])
            else:
                tmpList.pop(0)
                tmpList.append(tmpStr[i])
            n=0
            for x in tmpList:
                if ( 0 if x[18]=='' else float(x[18]))>90:
                    n+=1
            
            if n>=7:
                f=open(CsvPath+'result.txt','a')
                f.writelines((CellLine[0]+"|"+CellLine[1]+"|"+"通过"
                    +"|"+"日期:"+tmpList[0][0]+",无线接入性:"+tmpList[0][18]+'%'
                    +"|"+"日期:"+tmpList[1][0]+",无线接入性:"+tmpList[1][18]+'%'
                    +"|"+"日期:"+tmpList[2][0]+",无线接入性:"+tmpList[2][18]+'%'
                    +"|"+"日期:"+tmpList[3][0]+",无线接入性:"+tmpList[3][18]+'%'
                    +"|"+"日期:"+tmpList[4][0]+",无线接入性:"+tmpList[4][18]+'%'
                    +"|"+"日期:"+tmpList[5][0]+",无线接入性:"+tmpList[5][18]+'%'
                    +"|"+"日期:"+tmpList[6][0]+",无线接入性:"+tmpList[6][18]+'%\n'))
                f.close
                break


# GSM 切出成功率
    if CellLine[2]=='GSM切出差' or CellLine[2]=='GSM切出差小区'  :
        tmpStr=DataDict[CellLine[5]]
        tmpStr=sorted(tmpStr)
        if len(tmpStr)>=7:
            

            tmpList=[]
            tmpList.append(tmpStr[0])
            tmpList.append(tmpStr[1])
            tmpList.append(tmpStr[2])
            tmpList.append(tmpStr[3])
            tmpList.append(tmpStr[4])
            tmpList.append(tmpStr[5])
            for i in range(6,len(tmpStr)):
                if len(tmpList)<7:
                    tmpList.append(tmpStr[i])
                else:
                    tmpList.pop(0)
                    tmpList.append(tmpStr[i])
                n=0
                for x in tmpList:
                    if ( 0 if x[59]=='' else float(x[59]))>95:
                        n+=1
                
                if n>=7:
                    f=open(CsvPath+'result.txt','a')
                    f.writelines((CellLine[0]+"|"+CellLine[1]+"|"+"通过"
                        +"|"+"日期:"+tmpList[0][0]+",切出成功率:"+tmpList[0][59]+'%'
                        +"|"+"日期:"+tmpList[1][0]+",切出成功率:"+tmpList[1][59]+'%'
                        +"|"+"日期:"+tmpList[2][0]+",切出成功率:"+tmpList[2][59]+'%'
                        +"|"+"日期:"+tmpList[3][0]+",切出成功率:"+tmpList[3][59]+'%'
                        +"|"+"日期:"+tmpList[4][0]+",切出成功率:"+tmpList[4][59]+'%'
                        +"|"+"日期:"+tmpList[5][0]+",切出成功率:"+tmpList[5][59]+'%'
                        +"|"+"日期:"+tmpList[6][0]+",切出成功率:"+tmpList[6][59]+'%\n'))
                    f.close
                    break

#  GSM数据业务专项 下行TBF掉线率

    if CellLine[2]=='GSM数据业务专项' and ('下行TBF掉线率:' in CellLine[4]) :
        tmpStr=DataDict[CellLine[5]]
        tmpStr=sorted(tmpStr)
        if len(tmpStr)>=7:
            tmpList=[]
            tmpList.append(tmpStr[0])
            tmpList.append(tmpStr[1])
            tmpList.append(tmpStr[2])
            tmpList.append(tmpStr[3])
            tmpList.append(tmpStr[4])
            tmpList.append(tmpStr[5])
            for i in range(6,len(tmpStr)):
                if len(tmpList)<7:
                    tmpList.append(tmpStr[i])
                else:
                    tmpList.pop(0)
                    tmpList.append(tmpStr[i])
                n=0
                for x in tmpList:
                    if ( 0 if x[54]=='' else float(x[54]))<10:
                        n+=1
                
                if n>=7:
                    f=open(CsvPath+'result.txt','a')
                    f.writelines((CellLine[0]+"|"+CellLine[1]+"|"+"通过"
                        +"|"+"日期:"+tmpList[0][0]+",下行TBF掉线率:"+tmpList[0][54]+'%'
                        +"|"+"日期:"+tmpList[1][0]+",下行TBF掉线率:"+tmpList[1][54]+'%'
                        +"|"+"日期:"+tmpList[2][0]+",下行TBF掉线率:"+tmpList[2][54]+'%'
                        +"|"+"日期:"+tmpList[3][0]+",下行TBF掉线率:"+tmpList[3][54]+'%'
                        +"|"+"日期:"+tmpList[4][0]+",下行TBF掉线率:"+tmpList[4][54]+'%'
                        +"|"+"日期:"+tmpList[5][0]+",下行TBF掉线率:"+tmpList[5][54]+'%'
                        +"|"+"日期:"+tmpList[6][0]+",下行TBF掉线率:"+tmpList[6][54]+'%\n'))
                    f.close
                    break


#  GSM数据业务专项 EDGE下行IP吞吐率

    if CellLine[2]=='GSM数据业务专项' and ('EDGE下行IP吞吐率:' in CellLine[4]) :
        tmpStr=DataDict[CellLine[5]]
        tmpStr=sorted(tmpStr)
        if len(tmpStr)>=7:  
            tmpList=[]
            tmpList.append(tmpStr[0])
            tmpList.append(tmpStr[1])
            tmpList.append(tmpStr[2])
            tmpList.append(tmpStr[3])
            tmpList.append(tmpStr[4])
            tmpList.append(tmpStr[5])
            for i in range(6,len(tmpStr)):
                if len(tmpList)<7:
                    tmpList.append(tmpStr[i])
                else:
                    tmpList.pop(0)
                    tmpList.append(tmpStr[i])
                n=0
                for x in tmpList:
                    if ( 0 if x[55]=='' else float(x[55]))>30:
                        n+=1
                
                if n>=7:
                    f=open(CsvPath+'result.txt','a')
                    f.writelines((CellLine[0]+"|"+CellLine[1]+"|"+"通过"
                        +"|"+"日期:"+tmpList[0][0]+",EDGE下行IP吞吐率:"+tmpList[0][55]+''
                        +"|"+"日期:"+tmpList[1][0]+",EDGE下行IP吞吐率:"+tmpList[1][55]+''
                        +"|"+"日期:"+tmpList[2][0]+",EDGE下行IP吞吐率:"+tmpList[2][55]+''
                        +"|"+"日期:"+tmpList[3][0]+",EDGE下行IP吞吐率:"+tmpList[3][55]+''
                        +"|"+"日期:"+tmpList[4][0]+",EDGE下行IP吞吐率:"+tmpList[4][55]+''
                        +"|"+"日期:"+tmpList[5][0]+",EDGE下行IP吞吐率:"+tmpList[5][55]+''
                        +"|"+"日期:"+tmpList[6][0]+",EDGE下行IP吞吐率:"+tmpList[6][55]+'\n'))
                    f.close
                    break

# #  GSM差感知小区 掉话率（不含切换）

#     if CellLine[2]=='GSM差感知小区' and ('掉话率（不含切换）:' in CellLine[4]) :
#         tmpStr=DataDict[CellLine[5]]
#         tmpStr=sorted(tmpStr)
#         if len(tmpStr)<14:
#             continue
#         tmpDate=[]
#         tmpData=[]
#         for i in range(len(tmpStr)-14):
#             for n in range(14):
#                 tmpDate.append(tmpStr[i+n][0])
#                 tmpData.append(tmpStr[i+n][24])
#             if countif(tmpData[0:7],5)<2 and countif(tmpData[7:14],5)<2:
#                 f=open(CsvPath+'result.txt','a')
#                 f.writelines(CellLine[0]+"|"+CellLine[1]+"|"+CellLine[5]+"\n")
#                 f.close
#                 break


#  GSM差感知小区 无线接入性

    if CellLine[2]=='GSM差感知小区' and ('无线接入性:' in CellLine[4]) :
        tmpStr=DataDict[CellLine[5]]
        tmpStr=sorted(tmpStr)
        if len(tmpStr)>=7:
            tmpList=[]
            tmpList.append(tmpStr[0])
            tmpList.append(tmpStr[1])
            tmpList.append(tmpStr[2])
            tmpList.append(tmpStr[3])
            tmpList.append(tmpStr[4])
            tmpList.append(tmpStr[5])
            for i in range(6,len(tmpStr)):
                if len(tmpList)<7:
                    tmpList.append(tmpStr[i])
                else:
                    tmpList.pop(0)
                    tmpList.append(tmpStr[i])
                n=0
                for x in tmpList:
                    if ( 0 if x[18]=='' else float(x[18]))>80:
                        n+=1
                
                if n>=5:
                    f=open(CsvPath+'result.txt','a')
                    f.writelines((CellLine[0]+"|"+CellLine[1]+"|"+"通过"
                        +"|"+"日期:"+tmpList[0][0]+",无线接入性:"+tmpList[0][18]+'%'
                        +"|"+"日期:"+tmpList[1][0]+",无线接入性:"+tmpList[1][18]+'%'
                        +"|"+"日期:"+tmpList[2][0]+",无线接入性:"+tmpList[2][18]+'%'
                        +"|"+"日期:"+tmpList[3][0]+",无线接入性:"+tmpList[3][18]+'%'
                        +"|"+"日期:"+tmpList[4][0]+",无线接入性:"+tmpList[4][18]+'%'
                        +"|"+"日期:"+tmpList[5][0]+",无线接入性:"+tmpList[5][18]+'%'
                        +"|"+"日期:"+tmpList[6][0]+",无线接入性:"+tmpList[6][18]+'%\n'))
                    f.close
                    break

#  GSM差感知小区 掉话率（不含切换）

    if CellLine[2]=='GSM差感知小区' and ('掉话率（不含切换' in CellLine[4]) :
        tmpStr=DataDict[CellLine[5]]
        tmpStr=sorted(tmpStr)
        if len(tmpStr)>=7:
            tmpList=[]
            tmpList.append(tmpStr[0])
            tmpList.append(tmpStr[1])
            tmpList.append(tmpStr[2])
            tmpList.append(tmpStr[3])
            tmpList.append(tmpStr[4])
            tmpList.append(tmpStr[5])
            for i in range(6,len(tmpStr)):
                if len(tmpList)<7:
                    tmpList.append(tmpStr[i])
                else:
                    tmpList.pop(0)
                    tmpList.append(tmpStr[i])
                n=0
                for x in tmpList:
                    if float(x[24])<5:
                        n+=1
                
                if n>=5:
                    f=open(CsvPath+'result.txt','a')
                    f.writelines((CellLine[0]+"|"+CellLine[1]+"|"+"通过"
                        +"|"+"日期:"+tmpList[0][0]+",TCH掉话率（不含切换):"+tmpList[0][24]+'%'
                        +"|"+"日期:"+tmpList[1][0]+",TCH掉话率（不含切换):"+tmpList[1][24]+'%'
                        +"|"+"日期:"+tmpList[2][0]+",TCH掉话率（不含切换):"+tmpList[2][24]+'%'
                        +"|"+"日期:"+tmpList[3][0]+",TCH掉话率（不含切换):"+tmpList[3][24]+'%'
                        +"|"+"日期:"+tmpList[4][0]+",TCH掉话率（不含切换):"+tmpList[4][24]+'%'
                        +"|"+"日期:"+tmpList[5][0]+",TCH掉话率（不含切换):"+tmpList[5][24]+'%'
                        +"|"+"日期:"+tmpList[6][0]+",TCH掉话率（不含切换):"+tmpList[6][24]+'%\n'))
                    f.close
                    break


#  GSM高干扰

    if CellLine[2]=='GSM高干扰'  :
        tmpStr=DataDict[CellLine[5]]
        tmpStr=sorted(tmpStr)
        if len(tmpStr)>=28:
            tmpDataList=[]
            tmpDateList=[]
            for i in tmpStr:
                if i[48]=="":
                    tmpDataList.append(0)
                    tmpDateList.append(i[0])
                else:
                    tmpDataList.append(float(i[48]))
                    tmpDateList.append(i[0])
    
            for i in range(len(tmpDateList)-27):
                n=0
                if sum(tmpDataList[i:i+7])/7>30:
                    n+=1
                if sum(tmpDataList[i+7:i+14])/7>30:
                    n+=1
                if sum(tmpDataList[i+14:i+21])/7>30:
                    n+=1
                if sum(tmpDataList[i+21:i+28])/7>30:
                    n+=1
                if n<=1:
                    f=open(CsvPath+'result.txt','a')
                    f.writelines((CellLine[0]+"|"+CellLine[1]+"|"+"通过"
                        +"|"+"日期:"+tmpDateList[i]+"~"+tmpDateList[i+6]+'周粒度六忙时4、5级干扰比例:'+str(sum(tmpDataList[i:i+7])/7)+'%'
                        +"|"+"日期:"+tmpDateList[i+7]+"~"+tmpDateList[i+13]+'周粒度六忙时4、5级干扰比例:'+str(sum(tmpDataList[i+7:i+14])/7)+'%'
                        +"|"+"日期:"+tmpDateList[i+14]+"~"+tmpDateList[i+20]+'周粒度六忙时4、5级干扰比例:'+str(sum(tmpDataList[i+14:i+21])/7)+'%'                       
                        +"|"+"日期:"+tmpDateList[i+21]+"~"+tmpDateList[i+27]+'周粒度六忙时4、5级干扰比例:'+str(sum(tmpDataList[i+21:i+28])/7)+'%\n'))
                    f.close
                    break            


# GSM GSM TCH拥塞  GSM简报MVQ低接通
    if CellLine[2]=='GSM简报MVQ低接通'  or CellLine[2]=='GSM简报T拥塞' or CellLine[2]=='GSM TCH拥塞':
        tmpStr=DataDict[CellLine[5]]
        tmpStr=sorted(tmpStr)
        if len(tmpStr)<7:
            continue

        tmpList=[]
        tmpList.append(tmpStr[0])
        tmpList.append(tmpStr[1])
        tmpList.append(tmpStr[2])
        tmpList.append(tmpStr[3])
        tmpList.append(tmpStr[4])
        tmpList.append(tmpStr[5])
        for i in range(6,len(tmpStr)):
            if len(tmpList)<7:
                tmpList.append(tmpStr[i])
            else:
                tmpList.pop(0)
                tmpList.append(tmpStr[i])
            n=0
            for x in tmpList:
                if ( 0 if x[30]=='' else float(x[30]))<=5:
                    n+=1
            
            if n>=5:
                f=open(CsvPath+'result.txt','a')
                f.writelines((CellLine[0]+"|"+CellLine[1]+"|"+"通过"
                    +"|"+"日期:"+tmpList[0][0]+",TCH感知拥塞率:"+tmpList[0][30]+'%'
                    +"|"+"日期:"+tmpList[1][0]+",TCH感知拥塞率:"+tmpList[1][30]+'%'
                    +"|"+"日期:"+tmpList[2][0]+",TCH感知拥塞率:"+tmpList[2][30]+'%'
                    +"|"+"日期:"+tmpList[3][0]+",TCH感知拥塞率:"+tmpList[3][30]+'%'
                    +"|"+"日期:"+tmpList[4][0]+",TCH感知拥塞率:"+tmpList[4][30]+'%'
                    +"|"+"日期:"+tmpList[5][0]+",TCH感知拥塞率:"+tmpList[5][30]+'%'
                    +"|"+"日期:"+tmpList[6][0]+",TCH感知拥塞率:"+tmpList[6][30]+'%\n'))
                f.close
                break

# GSM 上行质差
    if ('质差' in CellLine[2])  and ('上行' in CellLine[4]):
        tmpStr=DataDict[CellLine[5]]
        tmpStr=sorted(tmpStr)
        if len(tmpStr)<7:
            continue

        tmpList=[]
        tmpList.append(tmpStr[0])
        tmpList.append(tmpStr[1])
        tmpList.append(tmpStr[2])
        tmpList.append(tmpStr[3])
        tmpList.append(tmpStr[4])
        tmpList.append(tmpStr[5])
        for i in range(6,len(tmpStr)):
            if len(tmpList)<7:
                tmpList.append(tmpStr[i])
            else:
                tmpList.pop(0)
                tmpList.append(tmpStr[i])
            n=0
            for x in tmpList:
                if ( 0 if x[71]=='' else float(x[71]))<=5:
                    n+=1
            
            if n>=5:
                f=open(CsvPath+'result.txt','a')
                f.writelines((CellLine[0]+"|"+CellLine[1]+"|"+"通过"
                    +"|"+"日期:"+tmpList[0][0]+",上行高质差:"+tmpList[0][71]+'%'
                    +"|"+"日期:"+tmpList[1][0]+",上行高质差:"+tmpList[1][71]+'%'
                    +"|"+"日期:"+tmpList[2][0]+",上行高质差:"+tmpList[2][71]+'%'
                    +"|"+"日期:"+tmpList[3][0]+",上行高质差:"+tmpList[3][71]+'%'
                    +"|"+"日期:"+tmpList[4][0]+",上行高质差:"+tmpList[4][71]+'%'
                    +"|"+"日期:"+tmpList[5][0]+",上行高质差:"+tmpList[5][71]+'%'
                    +"|"+"日期:"+tmpList[6][0]+",上行高质差:"+tmpList[6][71]+'%\n'))
                f.close
                break
                
# GSM 下行质差
    if ('质差' in CellLine[2])  and ('下行' in CellLine[4]):
        tmpStr=DataDict[CellLine[5]]
        tmpStr=sorted(tmpStr)
        if len(tmpStr)<7:
            continue

        tmpList=[]
        tmpList.append(tmpStr[0])
        tmpList.append(tmpStr[1])
        tmpList.append(tmpStr[2])
        tmpList.append(tmpStr[3])
        tmpList.append(tmpStr[4])
        tmpList.append(tmpStr[5])
        for i in range(6,len(tmpStr)):
            if len(tmpList)<7:
                tmpList.append(tmpStr[i])
            else:
                tmpList.pop(0)
                tmpList.append(tmpStr[i])
            n=0
            for x in tmpList:
                if ( 0 if x[71]=='' else float(x[71]))<=5:
                    n+=1
            
            if n>=5:
                f=open(CsvPath+'result.txt','a')
                f.writelines((CellLine[0]+"|"+CellLine[1]+"|"+"通过"
                    +"|"+"日期:"+tmpList[0][0]+",下行高质差:"+tmpList[0][74]+'%'
                    +"|"+"日期:"+tmpList[1][0]+",下行高质差:"+tmpList[1][74]+'%'
                    +"|"+"日期:"+tmpList[2][0]+",下行高质差:"+tmpList[2][74]+'%'
                    +"|"+"日期:"+tmpList[3][0]+",下行高质差:"+tmpList[3][74]+'%'
                    +"|"+"日期:"+tmpList[4][0]+",下行高质差:"+tmpList[4][74]+'%'
                    +"|"+"日期:"+tmpList[5][0]+",下行高质差:"+tmpList[5][74]+'%'
                    +"|"+"日期:"+tmpList[6][0]+",下行高质差:"+tmpList[6][74]+'%\n'))
                f.close
                break
