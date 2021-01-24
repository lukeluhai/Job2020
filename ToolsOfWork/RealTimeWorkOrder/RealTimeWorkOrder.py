import numpy
import pandas as pd
import xlrd
df_Issue=pd.DataFrame(pd.read_excel('e:\\RealTimeWorkOrder\\问题点跟踪.xlsx',sheet_name='方案库附件表-总表'),columns=['聚类工单序号','cgi','问题小区名','问题点指标','工单生成时间'])
print(df_Issue.dtypes)
df_CellAll=pd.DataFrame(pd.read_csv('e:\\RealTimeWorkOrder\\CellAll.csv',encoding='GBK',low_memory=False),columns=['子网ID','网元ID','E-UTRAN FDD小区ID','用户标识'])
print(df_CellAll.dtypes)

df_RelationAll=pd.DataFrame(pd.read_csv('e:\\RealTimeWorkOrder\\RelationAll.csv',encoding='GBK',low_memory=False),columns=['子网ID','网元ID','E-UTRAN FDD小区ID','E-UTRAN邻接小区'])

print(df_RelationAll.dtypes)
df_AlarAll=pd.read_csv('e:\\RealTimeWorkOrder\\大数据网管告警.csv',encoding='GBK',low_memory=False)
print(df_AlarAll)
df_Alarm=pd.read_csv('e:\\RealTimeWorkOrder\\告警标准名.csv',encoding='GBK')
df_AlarmList=pd.merge(df_AlarAll,df_Alarm,left_on='告警标准名',right_on='告警标准名',how='inner')
df_AlarmList=df_AlarmList.drop_duplicates()

print(df_AlarmList)
print(df_AlarmList.dtypes)
df_CellInfo=pd.read_csv('e:\\RealTimeWorkOrder\\小区基础信息.csv',encoding='GBK',low_memory=False)
print(df_CellInfo.dtypes)



s1=pd.merge(df_Issue,df_CellAll,left_on='问题小区名',right_on='用户标识',how='left')
s2=pd.merge(s1,df_RelationAll,left_on=['子网ID', '网元ID', 'E-UTRAN FDD小区ID'],right_on=['子网ID', '网元ID', 'E-UTRAN FDD小区ID'],how='left')
s3=pd.merge(s2,df_CellInfo,left_on='E-UTRAN邻接小区',right_on='CGI',how='left')
s4=pd.merge(s3,df_AlarmList,left_on='小区标识',right_on='小区名称',how='left')
s4['工单生成时间1']=pd.to_numeric(pd.to_datetime(s4['工单生成时间']))
s4['告警发生时间1']=pd.to_numeric(pd.to_datetime(s4['告警发生时间']))
s4['告警消除时间1']=pd.to_numeric(pd.to_datetime(s4['告警消除时间']))
s4['持续时间1']=(s4['告警消除时间1']-s4['告警发生时间1'])/1000/1000/1000/60/60/24
s4['持续时间2']=(s4['告警发生时间1']-s4['工单生成时间1'])/1000/1000/1000/60/60/24
s4.to_csv('e:\\RealTimeWorkOrder\\s4.csv')
s42=s4[s4['持续时间2']<-1]
s42=s42[s42['持续时间2']>-7]

s42=s42.groupby(['聚类工单序号','问题小区名'])['持续时间1'].max()
s42.to_csv('e:\\RealTimeWorkOrder\\s42.csv')
s43=pd.merge(s4,s42,left_on=['持续时间1'],right_on=['持续时间1'],how='inner')
s43.drop_duplicates(subset=['聚类工单序号','问题小区名'],inplace=True)
s43.to_csv('e:\\RealTimeWorkOrder\\s43.csv')
print(list(s43))
print(list(s1))
s5=pd.merge(s1,s43,left_on=['问题小区名','聚类工单序号'],right_on=['问题小区名','聚类工单序号'],how='left')
s5.drop_duplicates(subset=['聚类工单序号','问题小区名'],inplace=True)
s5.loc[s5['持续时间2']<-7,'持续时间1']='99999999'
s5.to_csv('e:\\RealTimeWorkOrder\\result.csv')


# s4=s[s4['持续时间']>1]
# s4=s[s4['持续时间']<]


print(s4.dtypes)
print(list(s5))
