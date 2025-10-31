""" Modify the list
Replace the 3rd element with 999.
Add 2 new numbers at the end.
Insert 111 at index 2.
Remove the first element. """

num=[1,2,3,4,5,6]
num[2]=999
num.extend([9,7])
num.insert(2,111)
num.pop(0)
print(num)
