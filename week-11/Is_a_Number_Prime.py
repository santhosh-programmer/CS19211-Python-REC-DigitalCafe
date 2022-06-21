# A prime number is an integer greater than one that is only divisible by one and itself. Write a function that determines whether or not its parameter is prime, returning True if it is, and False otherwise. 


import math
def isPrime(n):
    flag=0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            flag=1
            break
    if n==1 or flag==1:
        return False
    else:
        return True
        
            
    
