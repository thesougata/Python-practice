""" Create a function cube_of_number() that:
Takes a number as input inside the function.
Returns the cube of that number.
Call the function and print the result outside the function. """

def cube():
    a=int(input("number:"))
    b=a**3
    return(b)
hi=cube()
print("cube of that number is",hi)