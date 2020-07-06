import os
import time
c=[]
def secondsToStr(seconds):
    x = time.localtime(seconds)  # 时间元组
    return time.strftime("%Y-%m-%d %X", x)  # 时间元组转为字符串

a=os.listdir('E:\\temp\\照片\\')
for i in a:
    b=os.stat('E:\\temp\\照片\\'+i)
    print('文件创建时间:{}'.format(secondsToStr(b.st_ctime)))
    print('文件访问时间:{}'.format(secondsToStr(b.st_atime)))
    
    c.append([i,b.st_mtime])
print(c)

# for n in c:
#    os.utime('G:\\看图王\\'+n[0],(n[1],n[1]))