"""
Next problem (Problem 3 – forces break usage)

Write a function:

def count_until_zero(lis):
    ...

Rules:

Count numbers from the start of the list

Stop counting when you hit 0

Return how many numbers were counted before 0

If 0 never appears, return the length of the list

You must use break

Only one return, at the end

Example:

[3, 5, 7, 0, 9] → 3

[1, 2, 3] → 3

[0, 1, 2] → 0

This one will lock in break for you.
"""

def check_zero(liss):
    count = 0
    for each in liss:
        if each == 0:
            break
        count +=1
    return count




liss = [3, 5, 7,0, 9]
print(check_zero(liss))