a=["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]
b=input()
b=b[::-1]
b=int(b)
while(b>0):
    c=b%10
    print(a[c],end=" ")
    b//=10
