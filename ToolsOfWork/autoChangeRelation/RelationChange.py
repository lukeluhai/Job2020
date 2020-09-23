import numpy as np

import pandas as pd


dirpath="D:\\temp\\Relation\\"

p=pd.read_csv(dirpath+'MO_L_EUtranRelation31fdd.csv',encoding='GBK',header=0)
print(p['子网ID'],p['网元ID'])
p['newcol']=p['子网ID'].map(str)+'-'+p['网元ID'].map(str)
#cell=list(zip(p['子网ID'],p['网元ID'],p['E-UTRAN FDD小区ID'],p['E-UTRAN 邻接关系ID'],p['E-UTRAN邻接小区']))
print(p['newcol'])
# cellr=list(p['小区个体偏移'])
# a=dict(zip(cell,cellr))
# print(len(a))

