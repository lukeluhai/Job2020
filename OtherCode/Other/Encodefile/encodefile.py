import os
path=""
with open(path, "r+") as f:
   old = f.read()
   f.seek(0)
   f.write(data)
   f.write(old)