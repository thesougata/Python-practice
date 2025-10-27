# function to find a factorial
def fact(n):
    r=1
    for i in range(1,n+1):
        r*=i
    return r

print("factorial of the number",fact(5))