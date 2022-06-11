a=abs(int(input()))
b=len(str(a))
if b<=1:
    print("-1")
else:
    a=a//10
    print(a%10)
