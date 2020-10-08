import pandas as pd
import numpy as np


a=pd.read_csv('e:\\temp\\MO.csv',encoding='GBK')

print(type(a))
print(a.shape)
for i in range(9):
    print(a[i][6])
        