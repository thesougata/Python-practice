# Take 5 numbers from user input (space-separated) and store them in a list using list comprehension.
# From the same list, create another list that contains each number doubled using list comprehension.

nums=input("give 5 numbers separated with space:")
numbers=[int(x) for x in nums.split()]
print(numbers)

doubled = [x * 2 for x in numbers]
print(doubled)