"""Given:

words = ["apple", "ant", "banana", "bat", "ball"]


Build:

{
  "a": {5: ["apple"], 3: ["ant"]},
  "b": {6: ["banana"], 3: ["bat"], 4: ["ball"]}
}


Rules:
– values must be lists
– no sorting
– no comprehensions
– inner dict must be created when needed"""

words = ["apple", "ant", "banana", "bat", "ball"]
dih = {}

for each in words:
    if each[0] not in dih:
        dih[each[0]] = {}
    if len(each) not in dih[each[0]]:
        dih[each[0]][len(each)] = []
    dih[each[0]][len(each)].append(each)

print(dih)





#for each in words:
 #   if each[0] not in dih:
  #      dih[each[0]] = {}
   # if each
    #dih[each[0]][len(each)] = []


#for each in words:
 ##      dih[each[0]] = []
   # dih[each[0]].append(each)
#print(dih)
"""
for each in words:
    if len(each) not in dih:
        dih[len(each)] = []
    dih[len(each)].append(each)
print(dih)"""
