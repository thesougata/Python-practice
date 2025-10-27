""" Create a function is_prime(n) that:
Takes a number n as a parameter.
Returns True if n is a prime number, otherwise False.
Call it for a few numbers and print the results. """

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(is_prime(7))
print(is_prime(9))
print(is_prime(2))