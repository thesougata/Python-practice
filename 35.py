# Write a function that counts how many digits, even digits, and odd digits are in a number — and also returns their sum.

def operate(n):
    num=n
    d=0
    even=0
    odd=0
    sum_even=0
    sum_odd=0
    while num>0:
        digit=num%10
        d+=1
        if digit%2==0:
            even+=1
            sum_even+=digit
        else:
            odd+=1
            sum_odd+=digit
        num//=10
    return d,even,odd,sum_even,sum_odd

total,total_even,total_odd,even_sum,odd_sum=operate(8617647293)
print("total digits:",total,"total even digits:",total_even,",total odd digits:",total_odd,",sum of evens:",even_sum,",sum of odds",odd_sum)