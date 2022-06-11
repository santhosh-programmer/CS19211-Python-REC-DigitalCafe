a=int(input())
b=10
c=sum=1
if a==0:
    print("0")
else:
    for i in range(1,a):
        d=c
        c=b**i+d
        sum+=c
    print(sum)

