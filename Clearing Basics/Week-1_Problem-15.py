"""
logs = [
    ("/login", 120),
    ("/home", 80),
    ("/login", 200),
    ("/products", 150),
    ("/home", 110),
    ("/login", 90),
    ("/products", 300),
    ("/home", 70)
]
Your task
Create a dictionary where:

• each endpoint is a key
• the value contains:

total number of hits

average response time

Then sort the result by average response time (descending).

Expected structure (shape only)
arduino
Copy code
{
  "/products": {"count": X, "avg_time": Y},
  "/login": {"count": X, "avg_time": Y},
  "/home": {"count": X, "avg_time": Y}
}
Rules (important)
• Use defaultdict
• Do not hardcode endpoints
• Don’t compute average inside the loop
• Sorting should be done after aggregation

"""


"""

# old code without defaultdict

logs = [
    ("/login", 120),
    ("/home", 80),
    ("/login", 200),
    ("/products", 150),
    ("/home", 110),
    ("/login", 90),
    ("/products", 300),
    ("/home", 70)
]


dih = {}

for each in logs:
    ip = each[0]
    time = each[1]
    if ip not in dih:
        dih[ip] = {}
    dih[ip]["count"]=dih[ip].get("count", 0) + 1 
    if "avg_time" not in dih[ip]:
        dih[ip]["avg_time"]=[]

    dih[ip]["avg_time"].append(time)

for ip in dih:  
    dih[ip]["avg_time"] = sum(dih[ip]["avg_time"])/len(dih[ip]["avg_time"])

dih = sorted(dih.items(),key = lambda item: item[1]["avg_time"])

print(dih)


# new code with defaultdict
"""
from collections import defaultdict
logs = [
    ("/login", 120),
    ("/home", 80),
    ("/login", 200),
    ("/products", 150),
    ("/home", 110),
    ("/login", 90),
    ("/products", 300),
    ("/home", 70)
]

dih = defaultdict(lambda:defaultdict(int))

for each in logs:
    endpoint = each[0]
    time = each[1]
    dih[endpoint]["count"] = dih[endpoint].get("count", 0 ) + 1
    dih[endpoint]["avg_time"] = dih[endpoint].get("avg_time", 0) + time

for endpoint in dih:
    dih[endpoint]["avg_time"] = dih[endpoint]["avg_time"]/dih[endpoint]["count"]

dih = sorted(dih.items(), key = lambda item:item[1]["avg_time"], reverse=True)

print(dih)

