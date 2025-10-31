""" From your current list, create a new list that contains:
The square of even numbers only. """

num=input("give numbers with space:")
i=[int(x) for x in num.split()]
even=[a**2 for a in i if a%2==0 ]
print(even)

