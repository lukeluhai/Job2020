a={'a':1}
b={'b':2}
e={'e':3}
c=dict(a,**b)
d=dict(c,**e)

print(d)
