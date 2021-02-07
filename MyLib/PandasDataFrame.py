import pandas as pd 
import numpy
# 聚合字符串列
def groupByStr(df,list1,col):
    df.fillna('',inplace=True)
    df[col]=df.groupby(list1)[col].transform(lambda x:'|'.join(x))
    print(df.dtypes)
    print(type(df))
    return df


df_Issue = pd.DataFrame(
    pd.read_excel("e:\\RealTimeWorkOrder\\数据\\问题点跟踪.xlsx", sheet_name="方案库附件表-总表"),
    columns=["市领取人","聚类工单序号", "cgi", "问题小区名", "问题点指标", "工单生成时间"],
)

a=groupByStr(df_Issue,["市领取人"],"cgi")
print(a['cgi'])
a=a.reset_index()
print(a.dtypes)   

