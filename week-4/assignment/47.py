a=int(input())
b=len(str(a))
c=d=a
sum=0
for i in range(b):
    n=d%10
    sum+=n**(b-i)
    d=d//10
if sum==a:
    print("Yes")
else:
    print("No")
