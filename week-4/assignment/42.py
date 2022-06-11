a=int(input())
#close means 0 in list
#open means 1 in list
close=a #count of close
open=0 #count of open
b=[0]*(a+1)
for i in range(1,a+1,):
    for j in range(1,a+1,i):
        if(b[j]==0):
            b[j]=1
            close-=1
            open+=1
        else:
            b[j]=0
            close+=1
            open-=1
print("open =",open)
print("close =",close)
