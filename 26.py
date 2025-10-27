def sum_of_digits(n):
    num=n
    sum=0
    while num>0:
        digit=num%10
        sum+=digit
        num//=10
    return sum
s=sum_of_digits(123)
print(s)