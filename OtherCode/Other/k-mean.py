X=[(5.2,9.95),(7.07,8.15),(2.8,7.21),(7.64,4.24),(9.9,4.27),(5.28,6.23), \
   (7.37,3.12),(9.83,4.29),(4.54,1.57),(1,1.04),(2.7,3.77),(0.46,3.07),(8.48,4.58),(4.25,6.18), \
   (8.54,7.75),(9.45,8.25),(0.07,3.75),(4.28,4.46),(6.09,8.13),(9.41,8.01)]
x1,y1=0.07,3.75
x2,y2=7.07,8.15
x3,y3=9.41,8.01

D1=[]
D2=[]
D3=[]
DX1=[]
DX2=[]
DX3=[]
DY1=[]
DY2=[]
DY3=[]

for k in range(100):
    D1 = []
    D2 = []
    D3 = []
    DX1 = []
    DX2 = []
    DX3 = []
    DY1 = []
    DY2 = []
    DY3 = []
    for i in range(20):
       t1= ((X[i][0]-x1)**2+(X[i][1]-y1)**2)**0.5
       t2= ((X[i][0]-x2)**2+(X[i][1]-y2)**2)**0.5
       t3= ((X[i][0] - x3) ** 2 + (X[i][1] - y3) ** 2) ** 0.5
       if min(t1,t2,t3)==t1:
            D1.append(X[i])
            DX1.append(X[i][0])
            DY1.append(X[i][1])
       elif min(t1,t2,t3)==t2:
            D2.append(X[i])
            DX2.append(X[i][0])
            DY2.append(X[i][1])
       else:
            D3.append(X[i])
            DX3.append(X[i][0])
            DY3.append(X[i][1])

    x1,y1=sum(DX1)/len(DX1),sum(DY1)/len(DY1)
    x2,y2=sum(DX2)/len(DX2),sum(DY2)/len(DY2)
    x3,y3=sum(DX3)/len(DX3),sum(DY3)/len(DY3)


for i in D1:
    print(i)
print('-----------------------')
for i in D2:
    print(i)
print('-----------------------')
for i in D3:
    print(i)

