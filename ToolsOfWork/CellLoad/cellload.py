import numpy
import pandas as pd 
from sklearn.linear_model import LinearRegression

def replacePercent(x):
    return float(x.replace('%',''))/1.00



df= pd.read_csv('d:\\DataBase\\2020_10_04_19_07_26_819_gzyd_lwx_19739.csv',header=0,encoding='GBK')
print(df.shape)
df=df[df['eNodeB名称'].str.contains('DC')]
print(df.shape)
print(df['0416-下行PRB平均利用率'])
df=df[df['MR-RRC连接建立最大用户数_1488250261180-0-21']>20]
df=df[df['0416-下行PRB平均利用率'].map(replacePercent)<100]
df=df[df['0416-下行PRB平均利用率'].map(replacePercent)>0]

# df_x=df[['MR-RRC连接建立最大用户数_1488250261180-0-21','下行最大激活用户数','下行流量（GB)']]
df_x=df[['[FDD]下行QCI1平均激活用户数',	'[FDD]下行QCI2平均激活用户数'	,'[FDD]下行QCI3平均激活用户数',	'[FDD]下行QCI4平均激活用户数'	,'[FDD]下行QCI5平均激活用户数',	'[FDD]下行QCI6平均激活用户数',	'[FDD]下行QCI7平均激活用户数',	'[FDD]下行QCI8平均激活用户数'	,'[FDD]下行QCI9平均激活用户数']]
df_y=df['集团-下行PRB平均利用率  _1551403986592-1-4'].map(replacePercent)
print(df_y)
print(df_x.shape,df_y.shape)
model=LinearRegression()
# print(list(zip(df_x['MR-RRC连接建立最大用户数_1488250261180-0-21'],df_x['下行最大激活用户数'])))
result=model.fit(df_x,df_y)


print(model.intercept_)
print(model.coef_)
# print(df_x,df_y)