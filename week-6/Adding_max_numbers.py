# Write a program to add maximum number in both its row and column of a matrix. Find the maximum element row wise and maximum element column wise and add both the elements.

# Sample test case

# sample input

# 1  2  3

# 2  5  4

# 4  3  6

# Sample Output

# 11


a=[]
s=0
def colmax(c,i):
    for j in range(3):
        if(c<a[j][i]):
            c=a[j][i]
            break
    return c
for i in range(3):
    b=list(map(int,input().split()))
    a.append(b)
for i in range(0,3):
    c=max(a[i])
    if colmax(c,a[i].index(c))==c:
        s+=c
print(s)
