# Write a function to find the largest digit in a number.
def large(n):
    num=n
    l=0
    while num>0:
        digit=num%10
        if digit > l:
            l=digit
        num//=10
    print("largest one is",l)

large(98576)