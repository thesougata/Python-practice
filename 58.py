""" While Loop — Continue
Print numbers from 1 to 15 using a while loop.
Skip all even numbers using continue. """

a=1
while a <=15:
    if a%2==0:
        a+=1
        continue
    print(a)
    a+=1