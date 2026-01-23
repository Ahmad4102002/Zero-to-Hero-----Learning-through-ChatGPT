"""
Problem 2: Return vs Break (the other side of the coin)

Write a function:

def first_even(lis):
    ...


Rules:

Loop through the list

The moment you find the first even number, return it

If no even number exists, return None

Do not use break

You must use return inside the loop

Examples (expected behavior, not code):

If the list is [1, 3, 7, 4, 6] → output should be 4
If the list is [1, 3, 5] → output should be None
If the list is [] → output should be None

This problem is designed to teach you:

return stops the loop and the function

You don’t need break when return is enough

"""

def check_even(liss):

    for each in liss:
        if each % 2 == 0:
            return each
    return None




liss = [1, 3, 7]
print(check_even(liss))


