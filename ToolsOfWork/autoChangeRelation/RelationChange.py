import os
import pandas as pd
import numpy
path='E:\\relation\\'
dfRelation=pd.read_csv(path+'RelationAll.csv','r',encoding='GBK',delimiter=',',header=0)
print('maping....')
dfRelation['newcol1']=dfRelation['子网ID'].map(str)+'-'+dfRelation['网元ID'].map(str)+'-'+dfRelation['E-UTRAN FDD小区ID'].map(str)+'-'+dfRelation['E-UTRAN邻接小区']
print('maping....')
dfRelation['newcol2']=dfRelation['E-UTRAN 邻接关系ID'].map(str)+'|'+dfRelation['重选时相邻小区对服务小区偏差'].map(str)+'|'+dfRelation['小区个体偏移'].map(str)
print('dict relation....')
dictRelation=dict(zip(dfRelation['newcol1'],dfRelation['newcol2']))


dfCell=pd.read_csv(path+'CellAll.csv',encoding='GBK',delimiter=',',header=0)

# dfCell['newcol1']=dfCell['子网ID'].map(str)+'-'+dfCell['网元ID'].map(str)+'-'+dfCell['E-UTRAN FDD小区ID'].map(str)
dfCell['newcol2']=dfCell['子网ID'].map(str)+'-'+dfCell['网元ID'].map(str)+'-'+dfCell['E-UTRAN FDD小区ID'].map(str)+'-'+dfCell['eNodeB标识'].map(str)
# dictMoCell=dict(zip(dfCell['newcol1'],dfCell['用户标识']))
dictCellMo=dict(zip(dfCell['用户标识'],dfCell['newcol2']))

dfCell['CGI']='460:00:'+dfCell['eNodeB标识'].map(str)+":"+dfCell['小区标识'].map(str)
dictCGICell=dict(zip(dfCell['CGI'],dfCell['用户标识']))
dictCGIMo=dict(zip(dfCell['CGI'],dfCell['newcol2']))
dictMoCgi=dict(zip(dfCell['newcol2'],dfCell['CGI']))
print('open 切换统计...')
f=open(path+'切换统计.csv','r')
resultlist=[]
resultlist.append(f.__next__().replace('\n','')+','+'邻小区名'+','+'正向参数'+','+'反向参数'+','+'正向子网ID'+','+'正向网元ID'+','+'正向eNodeB标识'+','+'正向E-UTRAN FDD小区ID'+','+'反向子网ID'+','+'反向网元ID'+','+'反向eNodeB标识'+','+'反向E-UTRAN FDD小区ID'+'\n')
row=0
for line in f.readlines():
    row+=1
    #print(row)
    ltemp=line.split(',')
    cellname=ltemp[9]
    try:
        cellmo=dictCellMo[cellname]
    except:
        cellmo=""
    if cellmo=="":
        continue
    cellmoinfo=cellmo.split('-')
    relationstr=cellmo[0:cellmo.rfind('-')]+'-'+ltemp[12][2:]
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
        reverRelation=dictRelation[reversecellmo[0:reversecellmo.rfind('-')]+'-'+reverseCgi]
    except:
        reverRelation=''    
    
    try:
        cellrmoinfo=dictCellMo[reversecellname].split('-')
    except:
        cellrmoinfo=['','','','',]


    # print(cellmoinfo)
    a=line.replace('\n','')+','+reversecellname+','+forwordRelation+','+reverRelation+','+cellmoinfo[0]+','+cellmoinfo[1]+','+cellmoinfo[2]+','+cellmoinfo[3]+','+cellrmoinfo[0]+','+cellrmoinfo[1]+','+cellrmoinfo[2]+','+cellrmoinfo[3]+'\n'
    resultlist.append(a)
print('输出结果')
resultfile=open(path+'result.csv','w+')
resultfile.writelines(resultlist)
f.close()
resultfile.close()


