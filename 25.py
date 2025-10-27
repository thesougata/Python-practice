# Function to Check Palindrome Number
# A palindrome number is a number that reads the same backward as forward.

def palin(n):
    num=n
    rev=0
    while num>0:
        digit=num%10
        rev =(rev*10)+digit
        num //=10
    if n==rev:
        return True
    else:
        return False

number=palin(121)
print(number)

""" Step	num	    digit	rev (new)
    1	    121	    1	    0×10+1 = 1
    2	    12	    2	    1×10+2 = 12
    3	    1	    1	    12×10+1 = 121
    End	    0	    –	    rev = 121 ✅ """
