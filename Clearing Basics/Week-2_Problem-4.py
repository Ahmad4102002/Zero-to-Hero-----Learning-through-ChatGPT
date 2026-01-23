"""

Problem 1 — forces break understanding (no return allowed)

Write a function that checks whether a list contains a negative number.

Rules:

You MUST use a loop

You MUST use break

You MUST NOT use return inside the loop

The function should return True or False at the end

Example:
has_negative([1, 3, -2, 4]) → True
has_negative([1, 2, 3]) → False

This problem teaches:
You break when the search is over, not when the function is over.

"""
def check_negative(lis):

    found = False

    for each in lis:
        if each < 0:
            found = True
            break
    return found
            
lis = [1, 3, 4]
print(check_negative(lis))

