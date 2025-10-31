""" numbers = (5, 10, 15, 20, 25, 30, 35)
Write a Python statement to:
Find the average value of all numbers in the tuple.
Print the maximum and minimum numbers. """

numbers = (5, 10, 15, 20, 25, 30, 35)
avg=sum(numbers)/len(numbers)
print("average of numbers in tuple numbers:",avg)
print("minimum in numbers:",min(numbers))
print("maximum in numbers:",max(numbers))