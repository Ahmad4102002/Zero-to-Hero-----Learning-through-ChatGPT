"""Given:

nums = [1, 2, 1, 3, 2, 1, 4, 3, 2]


Build:

{
  "odd":  {1: 3, 3: 2},
  "even": {2: 3, 4: 1}
}


Rules:
– still one loop
– still dictionary
– no repeated logic blocks
– readable  """

nums = [1, 2, 1, 3, 2, 1, 4, 3, 2]

dih ={}

for each in nums:
    if each % 2 == 1:
        if "odd" not in dih:
            dih["odd"] = {}
        dih["odd"][each] = dih["odd"].get(each, 0) + 1
    else:
        if "even" not in dih:
            dih["even"] = {}
        dih["even"][each] = dih["even"].get(each, 0) + 1

print(dih)


"""Given:

nums = [1, 2, 1, 3, 2, 1, 4, 3, 2]


Build the following dictionary using one loop only:

{
  "small": {1: 3, 2: 3},
  "large": {3: 2, 4: 1}
}

Rules

• Outer keys are derived, not present in the list
• "small" → numbers ≤ 2
• "large" → numbers > 2
• Inner dictionary stores counts of each number
• No pre-hardcoding values
• One loop only """

nums = [1, 2, 1, 3, 2, 1, 4, 3, 2]

dih = {}

for each in nums:
    if each <= 2:
        key = "small"
    else: 
        key = "large"  
    if key not in dih:
        dih[key] = {}
    dih[key][each]= dih[key].get(each, 0) + 1
print(dih)
