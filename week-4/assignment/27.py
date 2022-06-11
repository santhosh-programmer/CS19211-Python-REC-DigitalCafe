a=int(input())
b=a
while a>1:
    if a%2==0:
        a=a/2
        flag=1
    else:
        flag=2
        break
if flag==1:
    print(b,"is a number that can be expressed as power of 2.")
else:
    print(b,"cannot be expressed as power of 2.")
