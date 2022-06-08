""" Print the following pattern
Sample Input and Output
5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 """

a=int(input())
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print(end="\n")
    
