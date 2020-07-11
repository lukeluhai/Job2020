import bisect
import sys
HAYSTACK=[1,4,5,6,8,12,15,18,20,40,56,78]
NEEDLES=[1,2,10,22,34,67]
def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        # position=bisect_fn(HAYSTACK,needle)
        print(HAYSTACK)
if __name__=="__main__":
    demo(bisect.bisect_left)
    demo(bisect.bisect_right)
