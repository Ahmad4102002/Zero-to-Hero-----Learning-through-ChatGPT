"""
Given:
Each log is:
(ip, endpoint, timestamp_in_seconds)

If more than 5 requests hit the same endpoint from the same IP within any 10-second window, mark it as "RATE_LIMITED", otherwise "OK".

Here is the input:

logs = [
    ("192.168.1.1", "/login", 1),
    ("192.168.1.1", "/login", 2),
    ("192.168.1.1", "/login", 3),
    ("192.168.1.1", "/login", 4),
    ("192.168.1.1", "/login", 5),
    ("192.168.1.1", "/login", 6),
    ("192.168.1.1", "/home", 2),
    ("10.0.0.1", "/login", 1),
    ("10.0.0.1", "/login", 20)
]

Expected output shape (important)

Final result must be:

{
  "192.168.1.1": {
      "/login": "RATE_LIMITED",
      "/home": "OK"
  },
  "10.0.0.1": {
      "/login": "OK"
  }
}
"""

logs = [
    ("192.168.1.1", "/login", 1),
    ("192.168.1.1", "/login", 2),
    ("192.168.1.1", "/login", 3),
    ("192.168.1.1", "/login", 4),
    ("192.168.1.1", "/login", 5),
    ("192.168.1.1", "/login", 6),
    ("192.168.1.1", "/home", 2),
    ("10.0.0.1", "/login", 1),
    ("10.0.0.1", "/login", 20)
]

# old code without defaultdict
"""
dih = {}

for ip, endpoint , time_stamp in logs:
    if ip not in dih:
        dih[ip] = {}
    if endpoint not in dih[ip]:
        dih[ip][endpoint] = {}
    dih[ip][endpoint]["count"] = dih[ip][endpoint].get("count", 0) + 1
    dih[ip][endpoint]["last_access"] = time_stamp

print(dih)

result = {}

for ip , endpoints in dih.items():
    result[ip] = {}
    for endpoint , status in endpoints.items():
        if status['last_access'] <= 10 and status['count'] > 5:
            result[ip][endpoint] = "RATE_LIMITED"
        else:
            result[ip][endpoint] = "OK"
print(result)

"""


def freeze(d):
    if isinstance(d, defaultdict):
        return {k: freeze(v) for k, v in d.items()}
    return d

# new with defaultdict

from collections import defaultdict

dih = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

for ip, endpoint, access in logs:
    dih[ip][endpoint]['count'] += 1

    if "last_access" not in dih[ip][endpoint]:

        dih[ip][endpoint]['last_access'] = []

    dih[ip][endpoint]['last_access'].append(access)

final_dict = freeze(dih)
print(dih)


"""result = {}

for ip,endpoints in final_dict.items():
    result[ip] = {}
    for endpoint , data in endpoints.items():
        if data['last_access'] <=10 and data['count'] > 5:
            result[ip][endpoint] = "RATE_LIMITED"
        else:
            result[ip][endpoint] = "OK"
print(result)
"""