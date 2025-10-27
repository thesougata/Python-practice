""" Take a number n from the user.
Print all numbers from 1 to n
Skip numbers divisible by 4
Count how many numbers were printed
At the end, print the count """

n=int(input("write a number:"))
count=0
for i in range(1,n+1):
    if i%4==0:
        continue
    print(i)
    count+=1
print("total",count)
