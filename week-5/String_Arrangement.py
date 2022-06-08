""" Write a program to get 3 strings as input.

In the 1st string, replace the vowels with “
In the 2nd string, replace the consonants with *
In the third string, convert the lowercase letters to upper case.

Input Format:

Take 3 Strings from stdin

Output Format:

In the 1st string, replace the vowels with "
In the 2nd string, replace the consonants with *
In the third string, convert the lowercase letters to upper case.
Example Input:
Hello
Hi
GoodMorning

Output:
H"ll"
*i
GOODMORNING"""

a=input()
b=input()
c=input()
for i in a:
    if i in 'aeiou':
        print(i.replace(i,'"'),end="")
    else:
        print(i,end="")
print(end="\n")
for i in b:
    if i not in "aeiou":
        print(i.replace(i,'*'),end="")
    else:
        print(i,end="")
print(end="\n")
for i in c:
    print(i.upper(),end="")
