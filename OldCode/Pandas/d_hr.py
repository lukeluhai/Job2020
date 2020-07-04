import pandas as pd
import re
def nhiring(s):
    return(int(s.replace('　人','').strip()))
def nsalarylevel(s):
    k=0
    a=re.compile(r'\d+')
    aa=a.findall(s)
    if len(aa)==0:
        return 0
    else:

        for n in aa:
            k=k+float(n)
        return (k/len(aa))

def counthr():
    colname=['company','position','positiontype','workingplace','hiring','salarylevel','recruitmenttype','newcomer','gender','age','language','languagelevel','network','manufacturer','degree','experience','posttime','lasttime ']
    print('')
    hr_table=pd.read_table('telhr_1216_.txt',sep='\|',encoding='GBK',names=colname)

    hr_table['nhiring']=hr_table['hiring'].map(nhiring)
    hr_table['nsalarylevel']=hr_table['salarylevel'].map(nsalarylevel)
    countcompany=hr_table.groupby('company').sum()

    print(hr_table)

class aaa:
    __

if __name__ == '__main__':
    counthr()
    print('hello')