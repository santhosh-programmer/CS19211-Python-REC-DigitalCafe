# You are given an array of N integers, A1, A2, . . . , AN and an integer K. Return the of count of distinct numbers in all windows of size K.

# Input :

# 1 2 1 3 4 3

# 3

# Output :

# 2

# 3

# 3

# 2

# Explanation

# All windows of size K are

# [1, 2, 1]

# [2, 1, 3]

# [1, 3, 4]

# [3, 4, 3]


a=input().split()
b=int(input())
c=len(a)-b+1
for i in range(0,c):
    l=a[0+i:3+i]
    d={}
    for j in l:
        if j in d.keys():
            d[j]+=1
        else:
            d[j]=1
    print(len(d))
