# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array A is monotone increasing if for all i <= j, A[i] <= A[j]. An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

# Write a program if n array is monotonic or not. Print "True" if is monotonic or "False" if it is not. Array can be monotone increasing or decreasing

# Sample Input1

# 6578

# Sample Output1

# True

# Sample Input2

# 6543

# Sample Output2

# True

# Sample Input 3

# 6787

# Sample Output3

# False

a=input()
b=a.split()
c=0
d=0
for i in range(0,len(b)-1):
    if(b[i]>=b[i+1]):
        c+=1
    elif (b[i]<=b[i+1]):
        d+=1
if c==0 or d==0:
    print("True")
else:
    print("False")
