""" For Loop — Factorial
Take a number n as input.
Print factorial of that number using a for loop. """

n=int(input("give a number"))
fact=1
for i in range(1,n+1):
    fact*=i
print ("factorial is:",fact)