# An Armstrong number is a number that is equal to the sum of cubes (or power of digits count) of its digits.

def armstrong(num):
    temp=num
    sum=0
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if sum== num:
        return True
    else:
        return False
    
a=armstrong(153)
print(a)

""" 
    Step	temp	digit = temp % 10	sum += digit³	temp //= 10 → new temp
    1	    153	    3	                27	            15
    2	    15	    5	                152	            1
    3	    1	    1	                153	            0 
    """