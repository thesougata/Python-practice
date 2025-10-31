# Take a list of numbers and create a new list that stores only numbers divisible by 3.
num=input("give numbers with space:")
numbers=[int(x) for x in num.split()]
check=[x for x in numbers if x%3==0]
print("numbers divisible by 3:",check)