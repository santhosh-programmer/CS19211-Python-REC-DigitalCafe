# Write a Python function sumofsquares(m) that takes an integer m returns True if m is a sum of squares and False otherwise. (If m is not positive, your function should return False.)

# Here are some examples to show how your function should work.

# >>> sumofsquares(41)

# True

# >>> sumofsquares(30)

# False

# >>> sumofsquares(17)

# True


from math import *
def issquare(n):
    k = int(sqrt(n))
    return(k*k == n)
def sumofsquares(m):
    flag=0
    for i in range(1,m):
        if issquare(i)==1:
            if(issquare(m-i)==1):
                flag=1
                break
    if flag==1:
        return True
    else:
        return False

 
