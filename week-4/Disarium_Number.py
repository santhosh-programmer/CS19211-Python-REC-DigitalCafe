""" A Number is said to be Disarium number when the sum of its digit raised to the power of their respective positions becomes equal to the number itself. Write a program to print number is Disarium or not.

Input Format:

Single Integer Input from stdin.

Output Format:

Yes or No.

Example Input:

175

Output:

Yes

Explanation

1^1 + 7^2 +5^3 = 175

Example Input:

123

Output:

No"""

a=int(input())
b=0
c=a
d=a
sum=0
while(c>0):
    c=c//10
    b+=1
for i in range(b):
    n=d%10
    sum+=n**(b-i)
    d=d//10
if sum==a:
    print("Yes")
else:
    print("No")
    
