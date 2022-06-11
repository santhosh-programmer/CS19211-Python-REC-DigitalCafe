a=int(input())
b=[]
c=0
while(a>0):
    rem=a%10
    b.append(rem)
    a=a//10
for i in b:
    if(b.count(i)<2):
        c+=1
print(c)
    
