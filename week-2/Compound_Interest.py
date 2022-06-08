""" Pretend that you have just opened a new savings account that earns 4 percent interest per year. The interest that you earn is paid at the end of the year, and is added to the balance of the savings account. Write a program that begins by reading the amount of money deposited into the account from the user. Then your program should compute and display the amount in the savings account after 1, 2, and 3 years. Display each amount so that it is rounded to 2 decimal places.

Sample Input:

10000

Sample Output:

Balance as of end of Year 1: $10400.00.

Balance as of end of Year 2: $10816.00.

Balance as of end of Year 3: $11248.64."""

p=int(input())
print("Balance as of end of Year 1: ${:.2f}.".format(p*(1+0.04),"."))
print("Balance as of end of Year 2: ${:.2f}.".format(p*(1+0.04)**2,"."))
print("Balance as of end of Year 3: ${:.2f}.".format(p*(1+0.04)**3,"."))
