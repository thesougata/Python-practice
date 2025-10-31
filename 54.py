""" For Loop — Sum & Average
Take marks of 5 subjects as input (one by one).
Calculate total and average using a for loop. """

sum=0
for i in range (5):
    marks=int(input("subject marks:"))
    sum+=marks

print("sum is:",sum)
print("average is:",sum/5)