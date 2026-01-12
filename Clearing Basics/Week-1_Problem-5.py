"""Given:

words = ["apple", "banana", "avocado", "blueberry", "cherry"]


Group them by first character.

Expected shape:

{
  "a": ["apple", "avocado"],
  "b": ["banana", "blueberry"],
  "c": ["cherry"]
}


Rules:
– no sorting
– no defaultdict
– no comprehensions"""

words = ["apple", "banana", "avocado", "blueberry", "cherry"]

dih = {}

# old logic 

"""for each in words:
    if each[0] == "a":
        if dih["a"] not in dih:
            dih["a"] = []
        dih["a"].append(each)

    elif each[0] == "b":
        if dih["b"] not in dih:
            dih["b"] = []
        dih["b"].append(each)"""

# new logic 

for each in words:
    if each[0] not in dih:
        dih[each[0]] = []
    dih[each[0]].append(each)

print(dih)

