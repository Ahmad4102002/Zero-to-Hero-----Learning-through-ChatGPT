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


dih = {}

for ip, endpoint, time in logs:

    if ip not in dih:
        dih[ip] = {}
    if endpoint not in dih[ip]:
        dih[ip][endpoint] = []
    dih[ip][endpoint].append(time)

results = {}

for ip , endpoints in dih.items():
    results[ip] = {}
    for endpoint , nums in endpoints.items():
        nums.sort()
        results[ip][endpoint] = "OK"
        # If more than 5 requests hit the same endpoint from within any 10-second window, mark it as "RATE_LIMITED"
        left = 0 
        length = 0
        for r in range(len(nums)):
            while nums[r]-nums[left] > 10:
                left+=1
            length = (r-left) + 1
            if length > 5:
                results[ip][endpoint] = "RATE_LIMITED"
                break

print(results)
            
            



    
    