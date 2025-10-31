""" Conditional Statements
Take age as input.
Print: "Child", "Teenager", "Adult", "Senior Citizen" based on age ranges:
<13 → Child
13–19 → Teenager
20–59 → Adult
60+ → Senior Citizen """

age=int(input("what is your age"))

if age>0 and age<13:
    print("child")
elif age>=13 and age<=19:
    print("teenager")
elif age>=20 and age<=59:
    print("adult")
else:
    print("senior citizen")