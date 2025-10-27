# Write a function that reverses the digits of a number
def reverse(n):
    num=n
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num//=10
    return rev
r=reverse(8617647293)
print("reverse of that number is:",r)