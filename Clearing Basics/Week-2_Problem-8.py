"""
Day 8 – Problem 3: Global + Per-Endpoint Rate Limiting

You are building an API gateway.

Every incoming request has:
ip, endpoint, timestamp

You must enforce two independent limits at the same time.

Rule 1: Global rate limit (per IP)
An IP can make at most 10 requests in 60 seconds, across all endpoints combined.

Rule 2: Per-endpoint rate limit (per IP + endpoint)
The same IP can make at most 5 requests in 10 seconds to a single endpoint.

A request is ALLOWED only if both rules pass.
If either rule fails → request is BLOCKED.

What you are expected to design

You need two sliding windows:

One window tracks all requests per IP
Another window tracks requests per IP per endpoint

These two checks must be logically independent, just like dedup vs rate limiting earlier.

Data structures (important mental model)

You should naturally arrive at:

One dictionary like
global_requests[ip] -> list of timestamps

Another dictionary like
endpoint_requests[ip][endpoint] -> list of timestamps

If your brain already visualized this, that’s a very good sign.

Function signature
def handle_request(ip, endpoint, timestamp):
    # returns "ALLOWED" or "BLOCKED"


No prints inside logic. Return values only.

Sliding window behavior (must)

For global window:

keep only timestamps within last 60 seconds

For endpoint window:

keep only timestamps within last 10 seconds

You already know how to do this with:

while times[-1] - times[0] > window:
    times.pop(0)

Expected behavior example (mentally)

If an IP hits:

/login 5 times quickly → OK

/home 5 times quickly → OK

total becomes 10 → still OK

11th request anywhere → BLOCKED (global limit)

If an IP hits:

/login 6 times within 10 seconds → BLOCKED
Even if global limit is not exceeded.

"""

from collections import defaultdict

global_limiter = defaultdict(list)
local_limiter = defaultdict(lambda:defaultdict(list))

def handle_reuests(ip, endpoint , time_stamp):

    #global rate limiter 
    nums = global_limiter[ip]

    
    

    while nums and time_stamp-nums[0] > 60:
        nums.pop(0) 

    length = len(nums)
    if length >= 10:
        return "BLOCK_GLOBAL"
    
    
    #local rate limiter
    bums = local_limiter[ip][endpoint]
    
    

    while bums and time_stamp- bums[0] > 10:
        bums.pop(0)
    leng = len(bums)
    if leng >= 5:
        return "BLOCK_LOCAL"
    
    nums.append(time_stamp)
    bums.append(time_stamp)

    print(local_limiter)

    return "OK"

requests = [
    ("10.0.0.1", "/login", 1),
    ("10.0.0.1", "/login", 2),
    ("10.0.0.1", "/login", 3),
    ("10.0.0.1", "/login", 4),
    ("10.0.0.1", "/login", 5),   
    ("10.0.0.1", "/login", 6),  
    ("10.0.0.1", "/home", 7),
    ("10.0.0.1", "/home", 8),
    ("10.0.0.1", "/home", 9),
    ("10.0.0.1", "/home", 10),
    ("10.0.0.1", "/home", 11),   
    ("10.0.0.1", "/search", 12),
    ("10.0.0.2", "/login", 13),
    ("10.0.0.2", "/login", 14),
    ("10.0.0.2", "/login", 15),
]

for log in requests:
    print(handle_reuests(*log))