import os
path="d:\\迅雷下载\\GHKO-51拍摄花絮.wmv"
data='1'
data=data.encode()
with open(path, "rb+") as f:
   old = f.read()
   f.seek(0)
   f.write(old)
   print(len(old))
   f.write(data)
   print(len(data))


