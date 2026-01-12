"""
Given:

statuses = [200, 404, 500, 200, 403, 404, 200, 500, 500]


You must count:
– 2xx
– 4xx
– 5xx

Rules (read carefully):
– use one loop
– do NOT pre-fill the dictionary
– categories must be created inside the loop
– no hardcoded counts

Allowed hint:

code // 100


Before coding, fix the data shape in your head:

{"2xx": int, "4xx": int, "5xx": int}"""

statuses = [200, 404, 500, 200, 403, 404, 200, 500, 500]

new = {}
for each in statuses:
    if each // 100 == 2:
        new["2xx"] = new.get("2xx", 0) +1

    elif each // 100 == 4:
        new["4xx"] = new.get("4xx", 0) +1

    elif each // 100 == 5:
        new["5xx"] = new.get("5xx", 0) +1

print(new)
