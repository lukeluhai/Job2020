def knap_rec(weight,wlist,n):
    if weight == 0:
        return True
    if weight <0 or (weight >0 and n <1):
        return False
    if knap_rec(weight-wlist[n-1],wlist,n-1):
        print("Item "+str(n)+':',wlist[n-1])
        return True
    if knap_rec(weight,wlist,n-1):
        return True
    else:
        return False
if __name__=="__main__":
    wlist=[2,8,4,9,17,13,10]
    weight=20
    n=7
    print(knap_rec(weight,wlist,n))