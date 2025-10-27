def count_digits(n):
    num = n
    count = 0
    while num > 0:
        count += 1          # increase count by 1 for each digit
        num //= 10          # remove last digit
    return count

result = count_digits(12345)
print("Total digits:", result)
