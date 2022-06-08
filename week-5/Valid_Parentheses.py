""" Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.

Open brackets must be closed in the correct order.

Constraints:

1 <= s.length <= 10^4

s consists of parentheses only '()[]{}'."""

a=input()
b=a.count('[')
c=a.count(']')
d=a.count('{')
e=a.count('}')
f=a.count('(')
g=a.count(')')
if(b==c and d==e and f==g):
    print("true")
else:
    print("false")
