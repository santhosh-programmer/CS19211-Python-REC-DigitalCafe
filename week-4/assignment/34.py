a=int(input())
d=10
rev=0
while a>0:
    b=a%10
    rev=rev*d+b
    a=a//10
print(rev)
