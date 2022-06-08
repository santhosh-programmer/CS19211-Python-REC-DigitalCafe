""" Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome."""

a=input()
b=""
for i in a:
    if (i.isalnum()):
        b=b+i.lower()
c=b[::-1]
if c==b:
    print("1")
else:
    print("0")
