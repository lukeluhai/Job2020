import os
import datetime
filePath="E:\\temp\\cdd\\"
rldepCsv=open(filePath+"RLDEP.csv",'r',encoding='utf-8',errors='ignore')
rldepExtCsv=open(filePath+"RLDEP_EXT.csv",'r',encoding='utf-8',errors='ignore')
rldepCsvDic={}
rldepCheckResult=[]
rldepCheckResult.append('EXCHID_EXT,CELL_EXT,CGI_EXT,BSIC_EXT,BCCHNO_EXT,CGI,BSIC,BCCHNO'+'\n')

for i in rldepCsv:
    rldepCsvDic[i.split(',')[1]]=i.split(',')[2]+','+i.split(',')[3]+','+i.split(',')[4]
for i in rldepExtCsv:
    if i.split(',')[1] in rldepCsvDic:
        
        if i.split(',')[2]+','+i.split(',')[3]+','+i.split(',')[4]!=rldepCsvDic[i.split(',')[1]]:
            rldepCheckResult.append(i.split(',')[0]+','+i.split(',')[1]+','+i.split(',')[2]+','+i.split(',')[3]+','+i.split(',')[4]+','+rldepCsvDic[i.split(',')[1]]+'\n')
for i in rldepCheckResult:
    print(i)
rldepCsv.close()
rldepExtCsv.close()







rlcppCsv=open(filePath+"RLCPP.csv",'r',encoding='utf-8',errors='ignore')
rlcppExtCsv=open(filePath+"RLCPP_EXT.csv",'r',encoding='utf-8',errors='ignore')
rlcppCsvDic={}
rlcppCheckResult=[]
rlcppCheckResult.append('EXCHID_EXT,CELL_EXT,MSTXPWR_EXT,MSTXPWR'+'\n')

for i in rlcppCsv:
    rlcppCsvDic[i.split(',')[1]]=i.split(',')[5]
for i in rlcppExtCsv:
    if i.split(',')[1] in rlcppCsvDic:
        
        if i.split(',')[3].strip()!=rlcppCsvDic[i.split(',')[1]].strip():
            
            rlcppCheckResult.append(i.split(',')[0]+','+i.split(',')[1]+','+i.split(',')[3].strip()+','+rlcppCsvDic[i.split(',')[1]]+'\n')
for i in rlcppCheckResult:
    print(i)
rlcppCsv.close()
rlcppExtCsv.close()





rllhpCsv=open(filePath+"RLlhp.csv",'r',encoding='utf-8',errors='ignore')
rllhpExtCsv=open(filePath+"RLlhp_EXT.csv",'r',encoding='utf-8',errors='ignore')
rllhpCsvDic={}
rllhpCheckResult=[]
rllhpCheckResult.append('EXCHID_EXT,CELL_EXT,LAYER_EXT,LAYERTHR_EXT,LAYERHYST_EXT,PSSTEMP_EXT,PTIMTEMP_EXT,LAYER,LAYERTHR,LAYERHYST,PSSTEMP,PTIMTEMP'+'\n')

for i in rllhpCsv:
    rllhpCsvDic[i.split(',')[1]]=i.split(',')[3]+','+i.split(',')[4]+','+i.split(',')[5]+','+i.split(',')[6]+','+i.split(',')[7]
for i in rllhpExtCsv:
    if i.split(',')[1] in rllhpCsvDic:
        
        if i.split(',')[3].strip()+','+i.split(',')[4].strip()+','+i.split(',')[5].strip()+','+i.split(',')[6].strip()+','+i.split(',')[7].strip()!=rllhpCsvDic[i.split(',')[1]].strip():
            rllhpCheckResult.append(i.split(',')[0]+','+i.split(',')[1]+','+i.split(',')[3].strip()+','+i.split(',')[4].strip()+','+i.split(',')[5].strip()+','+i.split(',')[6].strip()+','+i.split(',')[7].strip()+','+rllhpCsvDic[i.split(',')[1]]+'\n')
for i in rllhpCheckResult:
    print(i)
rllhpCsv.close()
rllhpExtCsv.close()



rllopCsv=open(filePath+"RLlop.csv",'r',encoding='utf-8',errors='ignore')
rllopExtCsv=open(filePath+"RLlop_EXT.csv",'r',encoding='utf-8',errors='ignore')
rllopCsvDic={}
rllopCheckResult=[]
rllopCheckResult.append('EXCHID_EXT,CELL_EXT,BSPWR_EXT,BSRXMIN_EXT,BSRXSUFF_EXT,MSRXMIN_EXT,MSRXSUFF_EXT,BSTXPWR_EXT,BSPWR,BSRXMIN,BSRXSUFF,MSRXMIN,MSRXSUFF,BSTXPWR'+'\n')

for i in rllopCsv:
    rllopCsvDic[i.split(',')[1]]=i.split(',')[2]+','+i.split(',')[3]+','+i.split(',')[4]+','+i.split(',')[5]+','+i.split(',')[6]+','+i.split(',')[17]
for i in rllopExtCsv:
    if i.split(',')[1] in rllopCsvDic:
        if i.split(',')[2].strip()+','+i.split(',')[3].strip()+','+i.split(',')[4].strip()+','+i.split(',')[5].strip()+','+i.split(',')[6].strip()+','+i.split(',')[17].strip()!=rllopCsvDic[i.split(',')[1]].strip():
            
            rllopCheckResult.append(i.split(',')[0]+','+i.split(',')[1]+','+i.split(',')[2].strip()+','+i.split(',')[3].strip()+','+i.split(',')[4].strip()+','+i.split(',')[5].strip()+','+i.split(',')[6].strip()+','+i.split(',')[17].strip()+','+rllopCsvDic[i.split(',')[1]]+'\n')
for i in rllopCheckResult:
    print(i)
rllopCsv.close()
rllopExtCsv.close()




rldepResultFile= open(filePath+"rldepResult.csv", "w",encoding='utf-8',errors='ignore')
rldepResultFile.writelines(rldepCheckResult)
rldepResultFile.close()


rlcppResultFile= open(filePath+"rlcppResult.csv", "w",encoding='utf-8',errors='ignore')
rlcppResultFile.writelines(rlcppCheckResult)
rlcppResultFile.close()


rllopResultFile= open(filePath+"rllopResult.csv", "w",encoding='utf-8',errors='ignore')
rllopResultFile.writelines(rllopCheckResult)
rllopResultFile.close()

rllhpResultFile= open(filePath+"rllhpResult.csv", "w",encoding='utf-8',errors='ignore')
rllhpResultFile.writelines(rllhpCheckResult)
rllhpResultFile.close()
