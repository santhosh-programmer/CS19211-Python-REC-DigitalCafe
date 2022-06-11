a=int(input())
#close=0
#open=1
b=[0]*(a)
for i in range(1,a+1,):
    for j in range(0,a,i):
        if(b[j]==0):
            b[j]=1
        else:
            b[j]=0
print("open =",b.count(1))
print("close =",b.count(0))
