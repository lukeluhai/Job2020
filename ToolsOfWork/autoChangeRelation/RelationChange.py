import os
import pandas as pd
import numpy
path='E:\\relation\\'
dfRelation=pd.read_csv(path+'RelationAll.csv','r',encoding='GBK',delimiter=',',header=0)
dfRelation['newcol1']=dfRelation['子网ID'].map(str)+'-'+dfRelation['网元ID'].map(str)+'-'+dfRelation['E-UTRAN FDD小区ID'].map(str)+'-'+dfRelation['E-UTRAN邻接小区']
dfRelation['newcol2']=dfRelation['E-UTRAN 邻接关系ID'].map(str)+'-'+dfRelation['重选时相邻小区对服务小区偏差'].map(str)+'-'+dfRelation['小区个体偏移'].map(str)
dictRelation=dict(zip(dfRelation['newcol1'],dfRelation['newcol2']))

print('dict relation....')
dfCell=pd.read_csv(path+'CellAll.csv',encoding='GBK',delimiter=',',header=0)

dfCell['newcol1']=dfCell['子网ID'].map(str)+'-'+dfCell['网元ID'].map(str)+'-'+dfCell['E-UTRAN FDD小区ID'].map(str)
dictMoCell=dict(zip(dfCell['newcol1'],dfCell['用户标识']))
dictCellMo=dict(zip(dfCell['用户标识'],dfCell['newcol1']))

dfCell['CGI']='460:00:'+dfCell['eNodeB标识'].map(str)+":"+dfCell['小区标识'].map(str)
dictCGICell=dict(zip(dfCell['CGI'],dfCell['用户标识']))
dictCGIMo=dict(zip(dfCell['CGI'],dfCell['newcol1']))
dictMoCgi=dict(zip(dfCell['newcol1'],dfCell['CGI']))
print('open 切换统计...')
f=open(path+'切换统计.csv','r')
resultlist=[]
resultlist.append(f.__next__().replace('\n','')+','+'邻小区名'+','+'正向参数'+','+'反向参数'+'\n')

for line in f.readlines():
    ltemp=line.split(',')
    cellname=ltemp[9]
    try:
        cellmo=dictCellMo[cellname]
    except:
        cellmo=""
    relationstr=cellmo+'-'+ltemp[12][2:]
    try:
        forwordRelation=dictRelation[relationstr]
    except:
        forwordRelation=''

    try:
        reversecellmo=dictCGIMo[ltemp[12][2:]]
#        print(reversecellmo)
    except:
        reversecellmo=''
    try:
        reversecellname=dictCGICell[ltemp[12][2:]]
    except:
        reversecellname=''
    try:
        reverseCgi=dictMoCgi[cellmo]
#        print(reverseCgi)
    except:
        reverseCgi=''

    try:
        reverRelation=dictRelation[reversecellmo+'-'+reverseCgi]
    except:
        reverRelation=''    
    a=line.replace('\n','')+','+reversecellname+','+forwordRelation+','+reverRelation+'\n'
    resultlist.append(a)
print('输出结果')
resultfile=open(path+'result.csv','a')
resultfile.writelines(resultlist)
f.close()
resultfile.close()


