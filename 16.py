# Create a function count_odd() that prints all odd numbers from 1 to 30 and also prints the total count of odd numbers.

def count_odd():
    count=0
    for i in range(1,31):
        if i%2!=0:
            print(i)
            count+=1
    print("count of odd",count)
count_odd()


