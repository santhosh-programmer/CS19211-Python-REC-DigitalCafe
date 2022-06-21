# Given two lists, print all the common element of two lists.

# Note: Sort the list before printing.

# Examples:

# Input : 
# 1 2 3 4 5 
# 5 6 7 8 9
# Output : 
# 5

# Input : 
# 1 2 3 4 5 
# 6 7 8 9
# Output : 
# No common elements 


a=set(input().split())
b=set(input().split())
c=sorted(list(a&b))
if c==[]:
    print("No common elements")
else:
    for i in c:
     print(i,end=" ")
