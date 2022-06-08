""" Write a program that determines the name of a shape from its number of sides. Read the number of sides from the user and then report the appropriate name as part of a meaningful message. Your program should support shapes with anywhere from 3 up to (and including) 10 sides. If a number of sides outside of this range is entered then your program should display an appropriate error message.

Sample Input 1

3

Sample Output 1

That's a triangle

Sample Input 2

7

Sample Output 2

That's a heptagon

Sample Input 3

11

Sample Output 3

That number of sides is not supported by this program."""

a=int(input())
if a==3:
    print("That's a triangle")
elif a==4:
    print("That's a quadrilateral")
elif a==5:
    print("That's a pentagon")
elif a==6:
    print("That's a hexagon")
elif a==7:
    print("That's a heptagon")
elif a==8:
    print("That's a octagon")
elif a==9:
    print("That's a nanogon")
elif a==10:
    print("That's a decagon")
else:
    print("That number of sides is not supported by this program.")
