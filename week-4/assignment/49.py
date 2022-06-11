a=int(input())
b=int(input())
prime=0
for i in range(a,b+1):
    flag=1
    for j in range(2,int((i**0.5)+1)):
        if i%j==0:
            flag+=1
    if(flag==1):
        prime+=1
print(prime)
            
