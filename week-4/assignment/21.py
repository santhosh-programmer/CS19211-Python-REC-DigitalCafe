a=float(input())
b=float(input())
c=a-b
if c>0:
    print("Loss amount : Rs. %.2f"%(abs(c)))
elif a==b:
    print("No profit No loss")
else:
    print("Profit amount : Rs. %.2f"%(abs(c)))
