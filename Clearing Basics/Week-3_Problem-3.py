"""
Problem – 3: Per-User + Per-Endpoint Rate Limiter (OOP)

You are designing a rate limiter for an API gateway.

Each incoming request is represented as:

(timestamp, user_id, endpoint)

Timestamps are strictly increasing.

Objective:
Design a class-based rate limiter that enforces two limits simultaneously.

Rules:

Global per user limit
A user can make at most 10 requests in any 60-second window (across all endpoints)

Endpoint-specific limit
A user can make at most 5 requests to the same endpoint in any 10-second window

If either limit is violated, the request must be rejected.

Your task:
Design a class called RateLimiter with the following interface:

class RateLimiter:
    def allow_request(self, timestamp, user_id, endpoint):
        pass


allow_request should:

Return True if the request is allowed

Return False if the request is rate-limited

Important constraints:

Use efficient sliding window logic

Maintain independent state per user and per endpoint

Do not mutate state if a request is rejected

Order of checks matters (think about which limit should be checked first)

Example usage:

limiter = RateLimiter()

requests = [
    (1, "u1", "/login"),
    (2, "u1", "/login"),
    ...
]

for t, u, e in requests:
    print(limiter.allow_request(t, u, e))


This problem tests:
OOP design, nested state management, correct control flow, and real-world reasoning.

"""
from collections import defaultdict
class RateLimiter:
    def __init__(self):

        self.global_dict = defaultdict(list)
        self.local_dict = defaultdict(lambda:defaultdict(list))

    def allow_request(self, time_stamp, identifier, endpoint):
        
        # global rate limiter  : A user can make at most 10 requests in any 60-second window (across all endpoints)

        

        while self.global_dict[identifier] and time_stamp - self.global_dict[identifier][0] > 60:
            self.global_dict[identifier].pop(0)

        if len(self.global_dict[identifier]) >= 10:
            return False
        
        # local rate limiter : A user can make at most 5 requests to the same endpoint in any 10-second window

        

        while self.local_dict[identifier][endpoint] and time_stamp - self.local_dict[identifier][endpoint][0] > 10:
            self.local_dict[identifier][endpoint].pop(0)

        if len(self.local_dict[identifier][endpoint]) >= 5:
            return False

        self.global_dict[identifier].append(time_stamp)
        self.local_dict[identifier][endpoint].append(time_stamp)

        return True



limiter = RateLimiter()

requests = [
    (1, "u1", "/login"),
    (2, "u1", "/login"),
]
for each in requests:
    print(limiter.allow_request(*each))