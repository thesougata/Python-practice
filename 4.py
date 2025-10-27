# Take a number n from user, print its multiplication table.

n=int(input("write a number:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)