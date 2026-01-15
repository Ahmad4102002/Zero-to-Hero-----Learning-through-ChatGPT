"""
Given:

logs = [
  ("192.168.1.1", "/login", 200),
  ("192.168.1.1", "/login", 401),
  ("192.168.1.1", "/home", 200),
  ("10.0.0.1", "/login", 200),
  ("10.0.0.1", "/login", 500),
  ("10.0.0.1", "/home", 200),
  ("10.0.0.1", "/home", 404),
  ("10.0.0.1", "/home", 404)
]


Build using one loop only and defaultdict:

{
  "192.168.1.1": {
      "/login": {"success": 1, "client_error": 1},
      "/home":  {"success": 1}
  },
  "10.0.0.1": {
      "/login": {"success": 1, "server_error": 1},
      "/home":  {"success": 1, "client_error": 2}
  }
}

Rules

• Use defaultdict (nested)
• No if key not in dict
• One loop only
• Status categories:

2xx → "success"

4xx → "client_error"

5xx → "server_error"
"""



"""

# old code using normal dict

dih = {}

for each in logs:
    ip = each[0]
    endpoint = each[1]
    status = each[2]

    if status // 100 == 2:
        key = "success"
    elif status // 100 == 4:
        key = "client_error"
    elif status // 100 == 5:
        key = "server_error"
    
    if ip not in dih:
        dih[ip] = {}
    if endpoint not in dih[ip]:
        dih[ip][endpoint] = {} 
    dih[ip][endpoint][key] = dih[ip][endpoint].get(key , 0) + 1

print(dih)
"""
from collections import defaultdict

logs = [
  ("192.168.1.1", "/login", 200),
  ("192.168.1.1", "/login", 401),
  ("192.168.1.1", "/home", 200),
  ("10.0.0.1", "/login", 200),
  ("10.0.0.1", "/login", 500),
  ("10.0.0.1", "/home", 200),
  ("10.0.0.1", "/home", 404),
  ("10.0.0.1", "/home", 404)
]

# new code using defaultdict

dih = defaultdict(lambda:defaultdict(lambda:defaultdict(int)))

for each in logs:
    ip = each[0]
    endpoint = each[1]
    status = each[2]

    if status // 100 == 2:
        key = "success"
    elif status // 100 == 4:
        key = "client_error"
    elif status // 100 == 5:
        key = "server_error"

    dih[ip][endpoint][key] += 1
print(dih)
