# Write a function to check if a number is an Armstrong number.
def arms(n):
    num=n
    cube=0
    while num>0:
        digit =num%10
        cube+=digit**3
        num//=10
    if cube==n:
        return "Armstrong number"
    else:
        return "not Armstrong number"
a=arms(153)
print("number is",a)
