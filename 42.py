""" From [5, 10, 15, 20, 25], create a new list that stores:
"Even" if the number is even,
"Odd" if the number is odd. """
nums=[5,10,15,20,25]
check= ["even" if x%2==0 else "odd" for x in nums]


print(check)