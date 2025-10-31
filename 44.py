""" Take numbers [5, 12, 18, 7, 25, 30]
Create a new list that stores:
"High" if number > 20
"Medium" if 10 ≤ number ≤ 20
"Low" if number < 10 """

nums = [5, 12, 18, 7, 25, 30]
check = ["High" if x > 20 else "Medium" if x >= 10 else "Low" for x in nums]
print(check)
