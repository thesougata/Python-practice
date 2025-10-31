""" nums = [[10,20,30],[40,50,60],[70,80,90]]
Then:
Print the entire list.
Print only the second row.
Print the middle element (50).
Loop through the list and print all elements row by row. """

nums = [[10,20,30],[40,50,60],[70,80,90]]
print(nums)
print(nums[1])
print(nums[1][1])

for i in nums:
    for a in i:
        print(a,end=" ")
    print()