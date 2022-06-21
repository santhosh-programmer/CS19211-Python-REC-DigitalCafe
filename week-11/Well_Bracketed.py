# A string with parentheses is well bracketed if all parentheses are matched: every opening bracket has a matching closing bracket and vice versa.

# Write a Python function wellbracketed(s) that takes a string s containing parentheses and returns True if s is well bracketed and False otherwise.

# Hint: Keep track of the nesting depth of brackets. Initially the depth is 0. The depth increases with each opening bracket and decreases with each closing bracket. What are the constraints on the value of the nesting depth for the string to be wellbracketed?

# Here are some examples to show how your function should work.

# >>> wellbracketed("22)")

# False

# >>> wellbracketed("(a+b)(a-b)")

# True

# >>> wellbracketed("(a(b+c)-d)((e+f)")

# False


def wellbracketed(s):
    a=0
    for i in s:
        if i=='(':
            a+=1
        elif i==')':
            a-=1
    if a==0:
        return True
    else:
        return False
            
