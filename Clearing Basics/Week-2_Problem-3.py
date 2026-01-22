"""
Day 7 – Problem 2: Deduplication + Rate Limiting (Combined)

This is a real interview / real system problem.

Problem statement

You are building an API gateway.

Each incoming request has:

(ip, endpoint, request_id, timestamp_in_seconds)


Rules:

Deduplication rule

If the same request_id is seen again within 30 seconds, mark it as "DUPLICATE"

Rate limiting rule

If more than 5 requests hit the same IP + endpoint within any 10-second window, mark it as "RATE_LIMITED"

Priority

If a request is "DUPLICATE", return "DUPLICATE" immediately

Otherwise, apply rate limiting

Requests arrive in time order

Input
logs = [
    ("192.168.1.1", "/login", "r1", 1),
    ("192.168.1.1", "/login", "r2", 2),
    ("192.168.1.1", "/login", "r3", 3),
    ("192.168.1.1", "/login", "r4", 4),
    ("192.168.1.1", "/login", "r5", 5),
    ("192.168.1.1", "/login", "r6", 6),
    ("192.168.1.1", "/login", "r1", 7),   # duplicate
    ("192.168.1.1", "/home",  "r7", 8),
    ("192.168.1.1", "/login", "r8", 20)
]

Expected behavior

For each request, immediately print one of:

"DUPLICATE"
"RATE_LIMITED"
"OK"
"""
dih = {}
results = {}

def handle_reuest(ip,endpoint,identifier,time_stamp):
    
    if ip not in dih:
        dih[ip] = {}
    if endpoint not in dih[ip]:
        dih[ip][endpoint] = {}
    if identifier not in dih[ip][endpoint]:
        print(f"{identifier} : NEW")
    else:
        if time_stamp - dih[ip][endpoint][identifier] < 30:
            print(f"{identifier} : DUPLICATE")
        else:
            print(f"{identifier} : NEW")
    
    dih[ip][endpoint][identifier] = time_stamp


   
    if ip not in results:
       results[ip] = {}
    if endpoint not in results[ip]:
       results[ip][endpoint] = []
    results[ip][endpoint].append(time_stamp)

    nums = results[ip][endpoint]

    while nums[-1] - nums[0] > 10:
        nums.pop(0)
    
    length = len(nums)
    if length > 5:
        print("RATE_LIMITED")
    else:
        print("OK")


logs = [
    ("192.168.1.1", "/login", "r1", 1),
    ("192.168.1.1", "/login", "r2", 2),
    ("192.168.1.1", "/login", "r3", 3),
    ("192.168.1.1", "/login", "r4", 4),
    ("192.168.1.1", "/login", "r5", 5),
    ("192.168.1.1", "/login", "r6", 6),
    ("192.168.1.1", "/login", "r1", 7),   
    ("192.168.1.1", "/home",  "r7", 8),
    ("192.168.1.1", "/login", "r8", 20)
]

for log in logs:
    handle_reuest(*log)











