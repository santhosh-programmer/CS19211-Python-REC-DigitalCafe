a=int(input())
b=-1
c=1
def fact():
    global b,c
    e=b+c
    b=c
    c=e
    return e
for i in range(0,a):
    d=fact()
print(d)
    
    
