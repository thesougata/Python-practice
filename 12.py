""" Take a number n from the user.
Print all numbers from 1 to n
Skip numbers divisible by 3
Count how many numbers were printed
At the end, print: count """

i = 1
n = int(input("Write a number: "))
count = 0

while i <= n:
    if i % 3 == 0:
        i += 1          # increment BEFORE continue
        continue
    print(i)
    count += 1
    i += 1              # normal increment
print("Total numbers printed:", count)
