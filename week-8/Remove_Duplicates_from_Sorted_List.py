# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:

# Input: 
# 1 1 2
# Output: 
# 1 2


a=list(set(input().split()))
a.sort()
for i in a:
    print(i,end=" ")
