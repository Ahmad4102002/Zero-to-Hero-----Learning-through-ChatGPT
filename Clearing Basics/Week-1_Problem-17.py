"""
Given
logs = [
  ("192.168.1.1", "/login", 200),
  ("192.168.1.1", "/login", 401),
  ("192.168.1.1", "/login", 401),
  ("192.168.1.1", "/login", 200),
  ("10.0.0.1", "/login", 401),
  ("10.0.0.1", "/login", 401),
  ("10.0.0.1", "/login", 401),
  ("10.0.0.1", "/login", 200),
  ("10.0.0.1", "/login", 200)
]

Build
{
  "192.168.1.1": {
      "/login": "OK"
  },
  "10.0.0.1": {
      "/login": "BLOCK"
  }
}

Rules (very important)

• Count only 4xx responses
• If 4xx count ≥ 3 → "BLOCK"
• Else → "OK"

Constraints (backend-style)

• No hardcoded IPs or endpoints
• Use defaultdict
• Exactly two phases:

collect counts

decide state

• Do not decide inside the log loop
• Do not mutate while iterating
"""
logs = [
  ("192.168.1.1", "/login", 200),
  ("192.168.1.1", "/login", 401),
  ("192.168.1.1", "/login", 401),
  ("192.168.1.1", "/login", 200),
  ("10.0.0.1", "/login", 401),
  ("10.0.0.1", "/login", 401),
  ("10.0.0.1", "/login", 401),
  ("10.0.0.1", "/login", 200),
  ("10.0.0.1", "/login", 200)
]

# without defaultdict to test myself
"""
dih = {}

for ip,endpoint,status  in logs:

    if status // 100 == 2:
        key = "2xx" 
    else:
        key = "4xx" 

    if ip not in dih:
        dih[ip] = {}
    if endpoint not in dih[ip]:
        dih[ip][endpoint] = {}
    dih[ip][endpoint][key] = dih[ip][endpoint].get(key, 0) + 1

print(dih)
"""
from collections import defaultdict

dih = defaultdict(lambda:defaultdict(lambda:defaultdict(int)))
for ip,endpoint , status in logs:
    if status // 100 == 2:
        key = "2xx"
    else:
        key = "4xx"
    dih[ip][endpoint][key] += 1
    dih[ip][endpoint]['total'] += 1

print(dih)
 

result = {}

for ip , endpoints in dih.items():
    result[ip] = {}
    for endpoint , status_counts in endpoints.items():
        if status_counts['4xx'] >= (1/2*status_counts['total']):
            result[ip][endpoint] = "BLOCK"
        else:
            result[ip][endpoint] = "OK"
print(result)
