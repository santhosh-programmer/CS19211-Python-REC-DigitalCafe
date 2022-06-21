# In the game of Scrabble™, each letter has points associated with it. The total score of a word is the sum of the scores of its letters. More common letters are worth fewer points while less common letters are worth more points. The points associated with each letter are shown below:

# Points Letters

# 1 A, E, I, L, N, O, R, S, T and U

# 2 D and G

# 3 B, C, M and P

# 4 F, H, V, W and Y

# 5 K

# 8 J and X

# 10 Q and Z

# Write a program that computes and displays the Scrabble™ score for a word. Create a dictionary that maps from letters to point values. Then use the dictionary to compute the score.

# A Scrabble™ board includes some squares that multiply the value of a letter or the value of an entire word. We will ignore these squares in this exercise.

# Sample Input

# REC

# Sample Output

# REC is worth 5 points.


a={'A':1,'E':1,'I':1,'L':1,'N':1,'O':1,'R':1,'S':1,'T':1,'U':1,'D':2,'G':2,'B':3,'C':3,'M':3,'P':3,'F':4,'H':4,'V':4,'W':4,'Y':4,'K':5,'J':8,'X':8,'Q':10,'Z':10}
b=input()
s=0
for i in b:
   s+=a[i]
print(b,"is worth",s,"points.")
