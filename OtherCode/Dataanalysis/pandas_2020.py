import pandas as pd 

df = pd.read_csv('D:\\temp\\人工评估\\csv\\0215-0219.csv',delimiter=',',encoding='ANSI',index_col=[0,8],parse_dates=['DAY'])
# delimiter 制表符
# encoding 编码
# index_col 索引列
print(df.shape)
print(df.index)
print(df.index.names)

print(df)