import numpy as np

import pandas as pd


dirpath="D:\\temp\\Relation\\"

p=pd.read_csv(dirpath+'AllEUtranRelation.csv',encoding='GBK',header=0)

cell=list(zip(p['子网ID'],p['网元ID'],p['E-UTRAN FDD小区ID'],p['E-UTRAN 邻接关系ID'],p['E-UTRAN邻接小区']))
print(len(cell))
cellr=list(p['小区个体偏移'])
a=dict(zip(cell,cellr))
print(len(a))

