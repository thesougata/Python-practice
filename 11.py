""" Take a number n from the user.
Print all numbers from 1 to n using while loop
Count how many numbers were printed
At the end, print the count """
i=1
n=int(input("give a number:"))
count=0
while i<=n:
    print (i)
    i+=1
    count+=1
print("total numbers are:",count)

