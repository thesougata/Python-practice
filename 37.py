# Modifying Lists
# Create a list nums = [10, 20, 30, 40, 50]
nums=[10,20,30,40,50]

# Change the second item to 200.
nums[1]=(200)
print(nums)

# Replace 30 and 40 with 300 and 400.
nums[2:3]=(300,400)
print(nums)

# Add a new number 60 at the end of the list.
nums.append(60)
print(nums)

# Add a new number 15 at the beginning of the list.
nums.insert(0,15)
print(nums)

# Add multiple items [70, 80, 90] to the list using extend().
nums.extend([70, 80, 90])
print(nums)

# Remove the value 200 from the list.
nums.remove(200)
print(nums)

# Remove the item at index 2 using pop().
nums.pop(2)
print(nums)

# Delete the first item using del.
del nums[0]
print(nums)

# Clear all elements from the list.
nums.clear()
print(nums)

"""
Create a fresh list of fruits and perform all four:
Replace one
Append one
Insert one
Remove one
"""
fruits=["aam","jam","kola","lebu"]
# replace
fruits[2]="peyara"
print(fruits)

# append
fruits.append("angur")
print(fruits)

# insert
fruits.insert(2,"apel")
print(fruits)

# Remove one
fruits.remove("apel")
print(fruits)