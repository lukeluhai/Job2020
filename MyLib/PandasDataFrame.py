import pandas as pd 
import numpy
def groupByStr(df,list1,col):
    df[col]=df.groupby(list1)[col].transform(lambda x:' '.join(x))
    return df


    

