import pandas as pd 
import numpy
def groupByStr(df,list1,col):
    df[col]=df.groupby(list1)[col].transform(lambda x:' '.join(x))
    return df
a=pd.read_csv('e:\\lh\\a.csv',encoding='GBK')
b=groupByStr(a,['a1','a2'],'cell')
print(b)
    

