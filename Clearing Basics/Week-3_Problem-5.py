"""
Week 3 – Problem 4 (OOP + Design Thinking)

You are building a configurable API rate limiter.

Each endpoint has its own rate-limit rules.

Problem Statement

Design a RateLimiter class that supports per-endpoint limits.

Each request has:

timestamp

user_id

endpoint

Rules:

Rate limits differ by endpoint

Limits apply per user per endpoint

Example configuration:

/login → 3 requests in 10 seconds

/search → 10 requests in 10 seconds

/upload → 1 request in 60 seconds

Requirements

Rate-limit rules must be passed during initialization

No hardcoded limits inside allow_request

Old timestamps must be cleaned correctly

Return True if allowed, False if blocked

Maintain independent state per user per endpoint

Function Signature (you must keep this)
class RateLimiter:
    def __init__(self, endpoint_limits):
        pass

    def allow_request(self, timestamp, user_id, endpoint):
        pass

Example Input
endpoint_limits = {
    "/login":  (3, 10),
    "/search": (10, 10),
    "/upload": (1, 60)
}

limiter = RateLimiter(endpoint_limits)

requests = [
    (1, "u1", "/login"),
    (2, "u1", "/login"),
    (3, "u1", "/login"),
    (4, "u1", "/login"),   # should be blocked
]

Expected Output
True
True
True
False

Hints (read carefully)

You already solved 90% of this in the last problem

Think about:

where limits live

where timestamps live

Do not use global variables

"""
from collections import defaultdict

class RateLimiter:
    def __init__(self,endpoint_limits):
        self.endpoint_limits = endpoint_limits
        self.global_dict = defaultdict(lambda:defaultdict(list)) 

    def allow_request(self,time_stamp,identifier,endpoint):

        if endpoint not in self.endpoint_limits:
            return True

        limit, window = self.endpoint_limits[endpoint]
        
        while self.global_dict[identifier][endpoint] and time_stamp - self.global_dict[identifier][endpoint][0] > window:
            self.global_dict[identifier][endpoint].pop(0)
        if len(self.global_dict[identifier][endpoint]) >= limit:
            return False

        self.global_dict[identifier][endpoint].append(time_stamp)
        return True
                

    

endpoint_limits = {
    "/login":  (3, 10),
    "/search": (10, 10),
    "/upload": (1, 60)
}

limiter = RateLimiter(endpoint_limits)

requests = [
    (1, "u1", "/login"),
    (2, "u1", "/login"),
    (3, "u1", "/login"),
    (4, "u1", "/login"),
]

for each in requests:
    print(limiter.allow_request(*each))



