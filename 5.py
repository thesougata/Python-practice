# Take a number n from user, print factorial of numbers from 1 to n.
fact=1
n=int(input("give a num:"))
for i in range(1,n+1):
    fact*=i
print("factorial is:",fact)