import os
k=0
f = open('E:\\temp\\切换\\a.csv', 'r')
for i in f.readlines():
    if k==0:

        print(i)
        k=k+1

    if "DYXJMCN" in i:
        print(i)
f.close()
