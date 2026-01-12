"""
Given:

nums = [1, 2, 1, 3, 2, 1, 4, 3, 2]


Build:

{
  1: {"count": 3},
  2: {"count": 3},
  3: {"count": 2},
  4: {"count": 1}
}


Rules:
– one loop
– no second pass
– keys created during the loop"""

nums = [1, 2, 1, 3, 2, 1, 4, 3, 2]
dih = {}
for each in nums:
    # dih[each] = dih.get(each, 0) +1
    if each not in dih:
        dih[each] = {}

    dih[each]["count"] = dih[each].get("count",0) + 1
print(dih)






