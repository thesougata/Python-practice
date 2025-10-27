""" Create a function largest(a, b, c) that:
Takes three numbers as parameters.
Returns the largest of the three.
Call it for (10, 45, 32) and print the result. """

def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
l=largest(10,45,32)
print("largest is",l)