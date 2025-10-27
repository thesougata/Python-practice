""" Create a function is_even(n) that:
Takes a number n as a parameter.
Returns "Even" if the number is even, else "Odd".
Call this function for the numbers 10, 21, and 44, and print the results. """

def is_even(n):
    if n%2==0:
        return "EVEN"
    else:
        return "ODD"
a=is_even(44)
b=is_even(10)
c=is_even(21)
print("number is",a)
print("number is",b)
print("number is",c)