""" Determine the factors of a number (i.e., all positive integer values that evenly divide into a number).

Sample Input and Output

20

1 2 4 5 10 20"""

a=int(input())
for i in range(1,a+1):
    if a%i==0:
        print(i,end=" ")
