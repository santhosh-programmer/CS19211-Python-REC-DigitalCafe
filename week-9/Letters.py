# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# Input Format:

# The first line of the input contains a statement.

# Output Format:

# Print the number of upper case and lower case respectively separated by a space.

# Example:

# Input:

# Hello world!

# Output:

# 1 9


a=input()
d={'u':0,'l':0}
for i in a:
    if i.isupper():
        d['u']+=1
    elif i.islower():
        d['l']+=1
print(d['u'],end=" ")
print(d['l'])
