# Write a function to find the smallest digit in a number.
def small(n):
    num=n
    l=9
    while num>0:
        digit=num%10
        if digit < l:
            l=digit
        num//=10
    print("smallest one is",l)

small(657895412)