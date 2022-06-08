""" An integer, n, is said to be perfect when the sum of all of the proper divisors of n is equal to n. For example, 28 is a perfect number because its proper divisors are 1, 2, 4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28. 

If the given number is a perfect number then your program will return True. Otherwise it will return False."""

a=int(input())
sum=0
for i in range(1,a):
    if a%i==0:
        sum+=i
if sum==a:
    print("True")
else:
    print("False")
