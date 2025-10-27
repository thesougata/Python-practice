# Write a function to count how many even and odd digits are there in a number.

def find(n):
    num=n
    even=0
    odd=0
    while num>0:
        digit=num%10
        if digit %2==0:
            even+=1
        else:
            odd+=1
        num//=10
    print("even numbers:", even)
    print("odd numbers:",odd)

find(8617647293)