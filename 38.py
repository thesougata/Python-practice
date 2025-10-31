# Take 3–4 fruit names in one line, store them into a list, and print that list.

names=input("give three favourite fruits names separating with space:")
fruits=names.split()
print(fruits)

# Take 4–5 numbers in one line, store them into a list, and print their sum.

nums=input("write 5 numbers separating with space:")
numbers=[int(x) for x in nums.split()]
print("sum of your numbers is:",sum(numbers))