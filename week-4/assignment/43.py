a=int(input())
b=[3,4]
j=1
d=0
while(len(b)<a):
    c=[]
    temp=d
    d=len(b)
    for i in range(temp,len(b)):
        b.append(3*(10**j)+b[i])
        c.append(4*(10**j)+b[i])
    for i in c:
        b.append(i)
    j+=1
print(b[a-1])

