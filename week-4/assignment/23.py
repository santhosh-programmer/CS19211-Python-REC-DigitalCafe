a=int(input())
b=int(input())
if a==1:
    if b>=1000:
        print("%.0f"%(b-b*0.1))
    else:
        print(b)
if a==2:
    if b>=100:
        print("%d"%b-b*0.05)
    else:
        print(b)
if a==3:
    if b>=500:
        print("%d"%(b-b*0.1))
    else:
        print(b)
    
