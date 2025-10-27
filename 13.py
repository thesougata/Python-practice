""" Take a number n from the user.
Print all numbers from 1 to n
Skip numbers divisible by 4 (continue)
Stop the loop if the sum of printed numbers exceeds 50 (break)
Count how many numbers were printed
At the end, print:
The count
The sum """
i=1
n=int(input("give a number:"))
count=0
sum=0
while i<=n:
    if i%4==0:
        i+=1
        continue
    print(i)
    count+=1
    sum+=i
    i+=1
    if sum>50:
        break
print("count:",count)
print("sum:",sum)

