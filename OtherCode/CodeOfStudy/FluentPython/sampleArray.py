from array import array
from random import random
import collections.abc as abc

floats=array('d',(random() for i in range(10*7)))
fp=open('floats.bin','wb')
floats.tofile(fp)
fp.close()

my_dict={}
print(isinstance(my_dict,abc.Mapping))
hash
