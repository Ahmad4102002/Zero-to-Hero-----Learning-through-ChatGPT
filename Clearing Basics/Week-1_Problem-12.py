"""Given:

logs = [
  ("192.168.1.1", "/login", 200),
  ("192.168.1.1", "/login", 401),
  ("192.168.1.1", "/home", 200),
  ("10.0.0.1", "/login", 200),
  ("10.0.0.1", "/login", 500),
  ("10.0.0.1", "/home", 200),
  ("10.0.0.1", "/home", 404)
]


Build using one loop only:

{
  "192.168.1.1": {
      "/login": {"success": 1, "client_error": 1},
      "/home":  {"success": 1}
  },
  "10.0.0.1": {
      "/login": {"success": 1, "server_error": 1},
      "/home":  {"success": 1, "client_error": 1}
  }
}

Rules

• Outer key = IP
• Second-level key = endpoint
• Third-level key = derived status category

2xx → "success"

4xx → "client_error"

5xx → "server_error"
• Count occurrences
• One loop only
• No pre-created structures
• No hardcoding exact status codes """

logs = [
  ("192.168.1.1", "/login", 200),
  ("192.168.1.1", "/login", 401),
  ("192.168.1.1", "/home", 200),
  ("10.0.0.1", "/login", 200),
  ("10.0.0.1", "/login", 500),
  ("10.0.0.1", "/home", 200),
  ("10.0.0.1", "/home", 404)
]

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
    dih[ip][endpoint][key] = dih[ip][endpoint].get(key, 0) + 1

print(dih)
        
