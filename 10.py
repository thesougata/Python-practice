""" Take two numbers from the user: start and end.
Print all numbers from start to end
Skip numbers divisible by 2 or 7
Stop the loop if the square of the number is greater than 200
Count how many numbers were printed
Calculate the sum of numbers printed
At the end, print:
The count
The sum """

a=int(input("start number:"))
b=int(input("end number:"))
count=0
sum=0
for i in range(a,b+1):
    if i%2==0 or i%7==0:
        continue
    print(i)
    count+=1
    sum+=i
    if i*i>200:
        break
print("count:",count)
print("sum:",sum)

