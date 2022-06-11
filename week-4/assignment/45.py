def calculate(n):
    a=int(input())
    b=[]
    temp=0
    for i in range(2,a+1):
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
        if flag!=1:
            b.append(i)
            if(a-i) in b:
                temp=1
                break
    if temp==1:
        print("yes")
    else:
        print("no")
    n-=1
    if n>0:
        calculate(n)
n=int(input())
calculate(n)
