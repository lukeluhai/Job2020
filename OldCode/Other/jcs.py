import math
import collections
def entropy(rows:list)->float:
    '''
    计算数的熵
    '''
    result=collections.Counter()
    result.update(rows)
    rows_len=len(rows)
    assert rows_len
    #开始计算熵
    ent=0.0
    for r in result.values():
        p=float(r)/rows_len
        ent-=p*math.log2(p)
    return ent
