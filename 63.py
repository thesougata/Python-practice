""" For Loop — Counting
Print all even numbers between 1 to 50 using for loop. """

count=0
for i in range(1,51):
    if i%2==0:
        count+=1
print("total even are",count)