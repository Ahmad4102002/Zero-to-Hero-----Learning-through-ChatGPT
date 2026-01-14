"""
Given:

logs = [
  ("192.168.1.1", 200),
  ("192.168.1.1", 404),
  ("10.0.0.1", 200),
  ("192.168.1.1", 500),
  ("10.0.0.1", 404),
  ("10.0.0.1", 201)
]


Build using one loop only:

{
  "192.168.1.1": {
      "success": 1,
      "client_error": 1,
      "server_error": 1
  },
  "10.0.0.1": {
      "success": 2,
      "client_error": 1
  }
}

Rules

• Outer key = IP
• Inner key is derived from status code
• "success" → 2xx
• "client_error" → 4xx
• "server_error" → 5xx
• Do not hardcode status numbers
• One loop only
• No extra passes

"""
logs = [
  ("192.168.1.1", 200),
  ("192.168.1.1", 404),
  ("10.0.0.1", 200),
  ("192.168.1.1", 500),
  ("10.0.0.1", 404),
  ("10.0.0.1", 201)
]

dih = {}

for each in logs:
    ip = each[0]
    status = each[1]

    if status // 100 == 2:
        key = "success"
    elif status // 100 == 4:
        key = "client_error"
    elif status // 100 == 5:
        key = "server_error"

    if ip not in dih:
        dih[ip] = {}
    dih[ip][key]= dih[ip].get(key,0) + 1

print(dih)



