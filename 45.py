""" Take a list of numbers:
nums = [5, 12, 18, 7, 25, 30, 3, 14, 22]

Your task:
Using list comprehension, create a new list that stores:
"Even-High" if number is even and greater than 20
"Even-Low" if number is even and ≤ 20
"Odd" if number is odd """

nums=[5, 12, 18, 7, 25, 30, 3, 14, 22]
check=["even-high" if x%2==0 and x>20 else "even-low" if x%2==0 and x <=20 else "odd" for x in nums]

print(check)