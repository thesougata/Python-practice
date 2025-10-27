# Print all odd numbers between 1 and 50 and count them.

odd=0
for i in range (1,51):
    if i%2!=0:
        print(i)
        odd+=1

print("odd numbers:",odd)