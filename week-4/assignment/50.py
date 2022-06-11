a=int(input())
count=0
b=[]
while a>0:
    c=a%10
    if c not in b:
        b.append(c)
        count+=1
    a=a//10
print(count)
