""" Write a program that prints numbers from 1 to 50,but:
Skip all numbers divisible by 3
Stop the loop completely if a number is greater than 40 """

for i in range(1,51):
    if i%3==0:
        continue
    elif i>40:
        break
    print(i)