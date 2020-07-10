import pandas as pd
import numpy as np
import os

path='E:\\temp\\基础信息\\快配表0615\\快配表0615\\'
dframes=[]

for i in os.listdir(path):
    print(i)
    a=pd.read_excel(path+i,sheet_name=None)
    c=a['GGsmCell']
    dframes.append(c)
    
result = pd.concat(dframes)
result.to_csv('E:\\temp\\基础信息\\快配表0615\\GGsmCell.csv')
