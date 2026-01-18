"""

items = [('a',1),('b',2),('a',3),('c',4),('a',5),('b',6)]
TO DO :
    dih = {a:value,b:vaalue}

"""
from collections import defaultdict
items = [('a',1),('b',2),('a',3),('c',4),('a',5),('b',6)]

dih = {}

for each in items:
    key = each[0]
    value = each[1]


    dih[key] =  dih.get(key, 0) + value

print(dih)

dih = defaultdict(int)
for each in items:
    key = each[0]
    value = each[1]


    dih[key] += value
print(dih)




