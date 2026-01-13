"""
Given:

logs = [
  ("192.168.1.1", 200),
  ("192.168.1.1", 404),
  ("10.0.0.1", 200),
  ("192.168.1.1", 200),
  ("10.0.0.1", 500)
]


Build:

{
  "192.168.1.1": {"2xx": 2, "4xx": 1},
  "10.0.0.1":    {"2xx": 1, "5xx": 1}
}


Rules:
– outer key = IP
– inner key = status category
– count occurrences
– one loop only

"""
logs = [
  ("192.168.1.1", 200),
  ("192.168.1.1", 404),
  ("10.0.0.1", 200),
  ("192.168.1.1", 200),
  ("10.0.0.1", 500)
]

dih = {}

for each in logs:
    ip = each[0]
    status = str(each[1])
    
    if ip not in dih:
        dih[ip] = {}
    dih[ip][f"{status[0]}xx"] = dih[ip].get(f"{status[0]}xx", 0) + 1

print(dih)



    
