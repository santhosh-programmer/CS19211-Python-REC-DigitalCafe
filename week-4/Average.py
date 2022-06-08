""" In this exercise you will create a program that computes the average of a collection of values entered by the user. The user will enter 0 as a sentinel value to indicate that no further values will be provided. Your program should display an appropriate error message if the first value entered by the user is 0.

Hint: Because the 0 marks the end of the input it should not be included in the average.

Sample Input

1

2

3

4

5

0

The average is 3.0."""

i=5
a=0
avg=0
while(i!=0):
    i=int(input())
    avg+=i
    a+=1
print("The average is {:.1f}.".format(avg/(a-1)))
