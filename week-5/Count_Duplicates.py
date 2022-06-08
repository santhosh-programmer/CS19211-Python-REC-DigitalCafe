""" Write a program to count the duplicates in the given string.

Input Format:
Take String from stdin.

Output Format:
Display the duplicate character and the count of the character.

Example Input:
google

Output:
g:2
o:2"""

a=input()
c=""
for i in a:
    if(i.isalpha()):
        b=a.count(i)
        if b>1 and i not in c:
            c+=i
            print("{:s}:{:d}".format(i,b))
if c=="":
    print("Not Exists")
