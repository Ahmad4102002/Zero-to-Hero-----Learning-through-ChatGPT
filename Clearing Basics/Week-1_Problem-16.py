"""
Given:

logs = [
  ("192.168.1.1", "/login", 200),
  ("192.168.1.1", "/login", 404),
  ("192.168.1.1", "/home", 200),
  ("10.0.0.1", "/login", 200),
  ("10.0.0.1", "/login", 500),
  ("10.0.0.1", "/home", 200),
  ("10.0.0.1", "/home", 404),
  ("10.0.0.1", "/home", 404)
]


Build exactly this:

{
  "192.168.1.1": {
      "/login": "UNSTABLE",
      "/home":  "OK"
  },
  "10.0.0.1": {
      "/login": "UNSTABLE",
      "/home":  "UNSTABLE"
  }
}

Rules

• One pass to collect data
• You must derive status class (2xx / 4xx / 5xx)
• Final value is not a count, it’s a label

Label logic

• "OK" → only 2xx responses
• "UNSTABLE" → at least one 4xx or 5xx
"""

from collections import defaultdict

def freeze(d):
    if isinstance(d, defaultdict):
        return {k: freeze(v) for k, v in d.items()}
    return d

logs = [
  ("192.168.1.1", "/login", 200),
  ("192.168.1.1", "/login", 404),
  ("192.168.1.1", "/home", 200),
  ("10.0.0.1", "/login", 200),
  ("10.0.0.1", "/login", 500),
  ("10.0.0.1", "/home", 200),
  ("10.0.0.1", "/home", 404),
  ("10.0.0.1", "/home", 404)
]

dih = defaultdict(lambda:defaultdict(lambda:defaultdict(int)))

for each in logs:
    ip = each[0]
    endpoint = each[1]
    status = each[2]

    if status // 100 == 2:
        key = "2xx"
    elif status // 100 == 4:
        key = "4xx"
    elif status // 100 == 5:
        key = "5xx"

    dih[ip][endpoint][key] += 1

final_result = freeze(dih)
print(final_result)

result = {}

for ip,endpoints in dih.items():
    result[ip]= {}
    for endpoint, status_counts in endpoints.items():
        if "4xx" in status_counts or "5xx" in status_counts:
            result[ip][endpoint] = "UNSTABLE"
        else:
            result[ip][endpoint] = "OK"

print(result)



        



