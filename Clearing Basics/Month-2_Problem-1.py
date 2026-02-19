"""
Write a function that flattens a nested list of arbitrary depth.

Example:

input = [1, [2, 3], [4, [5, 6]], 7]

output = [1, 2, 3, 4, 5, 6, 7]


Requirements:

Must work for any level of nesting

Do NOT hardcode depth

Prefer recursion (best practice here)

Hint:

👉 Check if element is list → recursively flatten
👉 Else → append
"""

# CREATE A FUNCTION WHICH EXTRACTS ALL ELEMETS FROM A NESTED LIST


# def take_out(input:list):

#     # if element is spotted sen dthe element insde the function again 
    
    
#     for each in input:
#         if isinstance(each, list):
#             take_out(each)
#         else:
#             saved.append(each)

# take_out(input)
# print(saved)


input = [1, [2, 3], [4, [5, 6]], 7]


class Flatten:
    def __init__(self):
        self.saved = []

    def flatten(self,input):

        for each in input:
            if isinstance(each, list):
                self.flatten(each)  
            else:
                self.saved.append(each)
                
        return self.saved

f1 = Flatten()

print(f1.flatten(input))


