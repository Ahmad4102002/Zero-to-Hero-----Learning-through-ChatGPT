"""
Next problem (Problem 4 – forces return inside loop)

This one is subtle but very important.

Write:

def first_greater_than_10(lis):
    ...


Rules:

Return the first number greater than 10

If no such number exists, return -1

You must return as soon as you find the number

Examples:

[3, 7, 11, 2] → 11

[1, 5, 9] → -1

[12, 3, 15] → 12

This will cement early return, which is everywhere in real code.
"""

def first_greater_than_10(liss):
    for each in liss:
        if each > 10:
            return each
    return -1
liss = [3, 7, 2]
print(first_greater_than_10(liss))

