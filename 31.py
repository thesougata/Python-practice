# Write a function that calculates the sum of all even digits and the sum of all odd digits in a number.
def operation(n):
    num=n
    even=0
    odd=0
    while num>0:
        digit=num%10
        if digit %2==0:
            even+=digit
        else:
            odd+=digit
        num//=10
    return even,odd
sum_even,sum_odd=operation(8617647293)
print("sum of even:",sum_even,",sum of odd:",sum_odd)

if sum_even > sum_odd:
    print("Even sum is greater.")
elif sum_odd > sum_even:
    print("Odd sum is greater.")
else:
    print("Both sums are equal.")