"""Given:

nums = [1, 2, 1, 3, 2, 1, 4, 3, 2]


Build:

{
  "odd":  {1: 3, 3: 2},
  "even": {2: 3, 4: 1}
}


Rules:
– one loop
– no pre-filled dictionaries
– inner dictionaries created during the loop"""

nums = [1, 2, 1, 3, 2, 1, 4, 3, 2]
dih = {}
for each in nums:
    if each % 2 == 1: #odd
        if "odd" not in dih:
            dih["odd"] = {}
        dih["odd"][each] = dih["odd"].get(each, 0) + 1

    if each % 2 == 0: #even
        if "even" not in dih:
            dih["even"] = {}
        dih["even"][each] = dih["even"].get(each, 0) + 1



print(dih)