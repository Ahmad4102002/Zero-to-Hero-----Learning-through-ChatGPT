"""Given:

nums = [1, 2, 3, 4, 5, 6, 7]


Group numbers into:
– "odd"
– "even"

Expected shape:

{
  "odd":  [1, 3, 5, 7],
  "even": [2, 4, 6]
}
"""

nums = [1, 2, 3, 4, 5, 6, 7]

dih = {}


for each in nums:
    if each % 2 == 0: # even
        if "even" not in dih:
            dih["even"] = []
        dih["even"].append(each)
    elif each % 2 == 1: #odd

        if "odd" not in dih:
            dih["odd"] = []
        dih["odd"].append(each)


print(dih)
    

    
