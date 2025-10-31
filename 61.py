""" Comparison & Logical Operators
Take marks of Math and English.
Print:
"Passed both" → if marks >=50 in both
"Passed one" → if marks >=50 in any
"Failed both" → otherwise """

a=int(input("your math marks:"))
b=int(input("your eng marks:"))

if a>=50 and b>=50:
    print("passed both")
elif a>=50 or b>=50:
    print("passed one")
else:
    print("failed both")