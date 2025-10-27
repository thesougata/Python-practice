# Write a function to check if a number is a palindrome.
def palin(n):
    num=n
    rev=0
    while num>0:
        digit =num%10
        rev=rev*10+digit
        num//=10
    if n==rev:
        return "palindrome"
    else:
        return "not palindrome"

p=palin(1856581)
print("Number is",p)