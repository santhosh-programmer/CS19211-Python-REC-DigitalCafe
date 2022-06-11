a=input()
b=a.split()
c=float(b[len(b)-1])
if c>100000:
    print("Tax to be paid  %.2f"%(c*0.15))
elif c>50000 and c<=100000:
    print("Tax to be paid  %.2f"%(c*0.10))
elif c<=50000:
    print("Tax to be paid  %.2f"%(c*0.05))
