# Create a function square_numbers(n) that takes a number n as a parameter and prints the square of all numbers from 1 to n.
def square_num(n):
    for i in range(1,n+1):
        print(i**2)
square_num(5)