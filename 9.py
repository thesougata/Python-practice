""" Take a number n from the user.
Print all numbers from 1 to n
Skip numbers divisible by 3
Stop the loop if the sum of printed numbers exceeds 100
Count how many numbers were printed
At the end, print:
The count of numbers printed
The sum of numbers printed """

n=int(input("write a number:"))
sum=0
count=0
for i in range(1,n+1):
    if i%3==0:
        continue
    print(i)
    count+=1
    sum+=i
    if sum>100:
        break
print("count of numbers:",count)
print("sum of numbers:",sum)
