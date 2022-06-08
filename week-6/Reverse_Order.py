""" Write a program that reads integers from the user and stores them in a list. Use 0 as a sentinel value to mark the end of the input. Once all of the values have been read your program should display them (except for the 0) in reverse order, with one value appearing on each line.

Sample Input

33
11
22
55
44
0
Sample Output
55
44
33
22
11"""

a=1
b=[]
while(a!=0):
   a=int(input())
   b.append(a)
b.sort(reverse=True)
for i in b:
    if i!=0:
        print(i)
