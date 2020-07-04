

import re
import time
import datetime

import pandas as pd

class hrcontents:

    def __init__(self):
        self.num=0
        self.payment=0

def salary(a):
    n=0
    if a=='面议':
        return (0)
    else:
        pattern=re.compile(r'\d+')
        s=pattern.findall(a)
        if len(s)==0:
            return(0)
        else:
            for f in s:
                n=int(f)+n
            return(n/len(s))

def hiren(a):
    return(int(a.replace('　人','').strip()))
def workspace(a):
    return(str(a)[0:4])
def network(a):
    return(len(a.split(',')))

def covporttime(a):
    b=a.split('-')
    return(datetime.date(int(b[0]),int(b[1]),int(b[2])))
def counthr():

    dic_company={}
    #省份字典
    dic_position={"4256":"海外","1033":"台湾","1032":"澳门","1031":"香港","1030":"内蒙古","1029":"西藏","1028":"新疆","1027":"青海省","1026":"宁夏","1025":"广西省","1024":"甘肃省","1023":"陕西省","1022":"云南省","1021":"贵州省","1020":"江西省","1019":"海南省","1018":"湖南省","1017":"湖北省","1016":"福建省","1015":"安徽省","1014":"山东省","1013":"黑龙江","1012":"吉林省","1011":"辽宁省","1010":"河南省","1009":"四川省","1008":"山西省","1007":"河北省","1006":"江苏省","1005":"广东省","1004":"浙江省","1003":"重庆市","1002":"天津市","1001":"上海市","1000":"北京市"}
    #生成df
    dfshengfen=pd.DataFrame(dic_position,index=['省份'])
    #转置df
    dfsf=dfshengfen.T
    #增加列’代号‘
    dfsf['代号']=dfsf.index
    #print(dfsf)

    dic_workplace={}
    dic_network={}
    dic_factor={}
    colname=['NO','company','position','positiontype','workingplace','hiring','salarylevel','recruitmenttype',\
             'newcomer','gender','age','language','languagelevel','network','manufacturer','degree','experience',\
             'posttime','lasttime']
    #打开文件导入dataframe
    tb=pd.read_table('telhr_0101.txt',sep='\|\|',names=colname)
    #重新计算列
    tb['薪资']=tb['salarylevel'].map(salary)

    tb['招聘人数']=tb['hiring'].map(hiren)/tb['network'].map(network)
    tb['总招聘人数'] = tb['hiring'].map(hiren)
    #print(tb)
    tb['newstarttime']=tb['posttime'].map(covporttime)

    #删除2017年12月15日前的数据
    tb=tb[tb['newstarttime']>datetime.date(2017,12,15)]


    tb['tmp']=tb['薪资']*tb['招聘人数']
    print('GSM平均工资：')
    print(tb[(tb['network'].str.contains('GSM'))&(tb['薪资']>1)]['tmp'].sum()/tb[(tb['network'].str.contains('GSM'))&(tb['薪资']>1)]['招聘人数'].sum())
    print('WCDMA平均工资：')
    print(tb[(tb['network'].str.contains('WCDMA'))&(tb['薪资']>1)]['tmp'].sum()/tb[(tb['network'].str.contains('WCDMA'))&(tb['薪资']>1)]['招聘人数'].sum())
    print('4G-LTE平均工资：')
    print(tb[(tb['network'].str.contains('4G-LTE')) & (tb['薪资'] > 1)]['tmp'].sum() /
          tb[(tb['network'].str.contains('4G-LTE')) & (tb['薪资'] > 1)]['招聘人数'].sum())

    print('CDMA/EVDO平均工资：')
    print(tb[(tb['network'].str.contains('CDMA/EVDO')) & (tb['薪资'] > 1)]['tmp'].sum() /
          tb[(tb['network'].str.contains('CDMA/EVDO')) & (tb['薪资'] > 1)]['招聘人数'].sum())
    print('WLAN平均工资：')
    print(tb[(tb['network'].str.contains('WLAN')) & (tb['薪资'] > 1)]['tmp'].sum() /
          tb[(tb['network'].str.contains('WLAN')) & (tb['薪资'] > 1)]['招聘人数'].sum())

    print('GSM招聘人数：')
    print(int(tb[(tb['network'].str.contains('GSM'))]['招聘人数'].sum()))
    print('WCDMA招聘人数：')
    print(int(tb[(tb['network'].str.contains('WCDMA'))]['招聘人数'].sum()))
    print('4G-LTE招聘人数：')
    print(int(tb[(tb['network'].str.contains('4G-LTE'))]['招聘人数'].sum()))
    print('CDMA/EVDO招聘人数：')
    print(int(tb[(tb['network'].str.contains('CDMA/EVDO'))]['招聘人数'].sum()))
    print('WLAN招聘人数：')
    print(int(tb[(tb['network'].str.contains('WLAN'))]['招聘人数'].sum()))

    tb['tmp2']=tb['hiring'].map(hiren)
    tb['省份']=tb['NO'].map(workspace)
    #GROUPBY
    tb3=tb.groupby('省份')['tmp2'].sum()
    tb4=pd.DataFrame(tb3)

    print(type(tb4))
    tb4=tb4.sort_values(['tmp2'],ascending=False)
    # print(tb4[0:30])
    # print(tb.ix[1:10,['NO','tmp2']])
    tb5=pd.merge(tb,dfsf,how='left',left_on='省份',right_on='代号')
    tb6 = tb5.groupby('省份_y')['tmp2'].sum()
    tb7 = pd.DataFrame(tb6)
    tb7 = tb7.sort_values(['tmp2'],ascending=False)
    tb7.rename(columns={"tmp2":"省份招聘人数"},inplace=True)




    print(tb7)

    tb8 = tb.groupby('company')['总招聘人数'].sum()
    tb8=pd.DataFrame(tb8)
    tb8 = tb8.sort_values(['总招聘人数'],ascending=False)
    print(tb8)





if __name__ == '__main__':
    counthr()

    print('hello')