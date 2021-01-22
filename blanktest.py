import pandas as pd
import numpy as np


cellall=pd.read_csv('d:\\temp\\Relation\\AllEUtranCell.csv',encoding='GBK',header=0)
relation=pd.read_csv('d:\\temp\\Relation\\AllEUtranRelation.csv',encoding='GBK',header=0)
cell=pd.read_csv('d:\\temp\\Relation\\cell.txt',header=0)
a=pd.merge(cell,cellall,how='left',left_on='CELL',right_on='用户标识')
print(a.dtypes)
print(relation.dtypes)
b=pd.merge(a,relation,how='inner',on=['子网ID','网元ID','E-UTRAN FDD小区ID'])
print(list(b))

print(b)