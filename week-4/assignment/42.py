import math
a=int(input())
open=0
for i in range(1,math.floor(math.sqrt(a)+1)):
    open+=1
print("open =",open)
print("close =",a-open)

