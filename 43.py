""" Take a list of names = ["ram", "sita", "lakshman", "hanuman"]
Create a new list that stores each name in uppercase and also add the text " Ji" after each name. """

names = ["ram", "sita", "lakshman", "hanuman"]
add=[x.upper()+" Ji" for x in names ]
print (add)