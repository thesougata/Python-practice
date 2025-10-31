"""
Take your name, age, and MBA student status (yes/no) from user input.
Print a formatted statement: "My name is ___, age ___, MBA student: ___" 
""" 

a=input("what is your name:")
b=int(input("what is your age:"))
c=input("are you mba student? (yes/no)")
is_c=True if c.lower()=="yes" else False

print("My name is",a,"my age is",b,"MBA student:",is_c)