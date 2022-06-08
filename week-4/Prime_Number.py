""" The user is given two integer numbers, lower value, and upper value. The task is to write the Python program for printing all the prime numbers between the given interval (or range).

Sample Input and Output

2

7

2 3 5"""

a=int(input())
b=int(input())
for i in range(a,b+1):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
    if flag!=1:
        print(i,end=" ")
