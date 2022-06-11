a=int(input())
b=1
k=0
def add(b,i,j):
    print(b,end=" ")
    c=b+i
    if(j>0):
        j-=1
        add(c,i-1,j)
while(b<=a):
    i=a
    j=a-1-k
    add(b,i,j)
    b+=1
    k+=1
    print(end="\n")
    
