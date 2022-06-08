""" Write a program that reads an integer from the user. Then your program should display a message indicating whether the integer is even or odd.

Sample Input1:

5

Sample Output1:

5 is odd.

Sample Input2:

10

Sample Output2:

10 is even."""

a=int(input())
if a%2==0:
    print(a,"is even.")
else:
    print(a,"is odd.")
