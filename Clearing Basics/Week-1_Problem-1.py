"""
Problem 1 – Basic frequency (warm-up)

Given this list:

nums = [1, 2, 1, 3, 2, 1, 4, 3, 2]

Count how many times each number appears.

Rules:
– use a normal for loop
– use a dictionary
– no Counter
– no comprehensions

Before coding, write (mentally or as comment):
“What changes on each iteration?”

Expected shape:
{number: count} """

nums = [1, 2, 1, 3, 2, 1, 4, 3, 2]

uniue = {}

for each in nums:
    uniue[each] = uniue.get(each, 0) +1


print(uniue)
