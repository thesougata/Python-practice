""" Take two numbers from the user: start and end.
Print all numbers between start and end (inclusive)
Skip numbers divisible by 2 or 5
Stop the loop if a number becomes greater than 50
Count how many numbers were actually printed """

a=int(input("start number:"))
b=int(input("end number:"))
count=0

for i in range(a,b+1):
    if i%2==0 or i%5==0:
        continue
    elif i>50:
        break
    print(i)
    count+=1

print("total:",count)