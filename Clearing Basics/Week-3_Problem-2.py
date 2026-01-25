"""
Problem – 2: Rate Limiter (OOP Design)

You are building a reusable rate limiting system for an API.

Each request is represented as:

(timestamp, user_id)

Timestamps are strictly increasing.

Objective:
Design a class-based rate limiter that enforces limits per user.

Rule:
A user can make at most 5 requests in any 10-second window.
If the limit is exceeded, the request should be rejected.

Your task:
Design a class called RateLimiter with the following behavior.

The class must:

Maintain internal state per user

Use an efficient sliding window approach

Be reusable and extensible

Required Interface:

class RateLimiter:
    def allow_request(self, timestamp, user_id):
        pass


allow_request should:

Return True if the request is allowed

Return False if the request is rate-limited

Example usage:

limiter = RateLimiter()

requests = [
    (1, "u1"),
    (2, "u1"),
    (3, "u1"),
    (4, "u1"),
    (5, "u1"),
    (6, "u1"),
]

for t, u in requests:
    print(limiter.allow_request(t, u))


Expected output:

True
True
True
True
True
False


This problem tests:
Your understanding of OOP design, encapsulation, state management, and how to move logic from functions into classes.


Rule:
A user can make at most 5 requests in any 10-second window.
If the limit is exceeded, the request should be rejected.
"""
from collections import defaultdict

class RateLimiter:
    
    def __init__(self):
            self.dih = defaultdict(list)

    def allow_request(self, timestamp, user_id):
        

        while self.dih[user_id] and timestamp - self.dih[user_id][0] > 10:
            self.dih[user_id].pop(0)
        
        if len(self.dih[user_id]) >= 5:
            return False
        
        self.dih[user_id].append(timestamp)
        return True



        




limiter = RateLimiter()

requests = [
    (1, "u1"),
    (2, "u1"),
    (3, "u1"),
    (4, "u1"),
    (5, "u1"),
    (6, "u1"),
]

for t, u in requests:
    print(limiter.allow_request(t, u))