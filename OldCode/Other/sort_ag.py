import math


l=[93,54,77,31,44,55,226,1,8,4,100,35,67,59,25,1000,36,38,12,46,555,278]
ll=[93,54,77,31,44,55,226,1,8,4,100,35,67,59,25,1000,36,38,12,46,555,278]

def insert_sort(l):

    n=len(l)
    k=0
    for i in range(1,n):

        for j in range(i,0,-1):
            k=k+1
            if l[j]<l[j-1] :
                l[j],l[j-1]=l[j-1],l[j]
            else:
                break




    print(l)
    print(k)

def shell_sort(l):
    n=len(l)
    mm=0
    for i in [6,3,1]:

        for k in range(i - 1, -1, -1):

            for j in range(k,n,i):
                for m in range(j+i,0,-i):

                    if m<n and m-i>=0:
                        mm=mm+1
                        if l[m]<l[m-i]:
                            print(l[m],l[m-i])
                            print(l)
                            l[m],l[m-i]=l[m-i],l[m]
                            print(l)
                        else:
                            break











    print(l)
    print(mm)


def merge_sort(s):
    n=len(s)
    m=[]
    l=s

    for i in range(0,int(math.log(n,2)+2)):

        for j in range(0,n,2**i):

            #print(i,j,j*i)
            if (2**i*j+2**i)>n-1:
                left=l[j*2**i]
                right=l[n-1]
                while left<right:
                    if l[right]<l[left]:
                        m.append(l[right])
                        print("m", m,left,right)
                        right-=right
                    else:
                        m.append(l[left])
                        print("m", m,left,right)
                        left+=left
            else:
                left=2**i*j
                right=2**i*j+2**i
                while left<right:

                    print(l)
                    if l[right]<l[left]:
                        m.append(l[right])
                        print("m",m,left,right)
                        right-=right
                    else:
                        m.append(l[left])
                        print("m", m,left,right)
                        left+=left
        l=m
        m=[]






#insert_sort(ll)
#shell_sort(l)
merge_sort(l)
