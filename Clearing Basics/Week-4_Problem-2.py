"""
Week 4 – Problem 2: Tier-Based Rate Limiter (Free vs Premium)

You are extending your existing rate limiter to support user tiers.

Each request has:

timestamp

user_id

endpoint

user_tier ("free" or "premium")

Rate-Limiting Rules
Global limits

Free users → 20 requests per 60 seconds

Premium users → 100 requests per 60 seconds

Endpoint limits

Endpoint limits differ by tier.

Example configuration:

endpoint_limits = {
    "free": {
        "/login":  (3, 10),
        "/search": (10, 10)
    },
    "premium": {
        "/login":  (10, 10),
        "/search": (50, 10)
    }
}

Important Behavior Rules

Global limit is checked before endpoint limit

Blocked requests are never recorded

Global and endpoint windows are independent

Tier logic must be config-driven

No if tier == "free" hardcoding inside logic

Class Design (Must Use This)
class RateLimiter:
    def __init__(self, global_limits, endpoint_limits):
        pass

    def allow_request(self, timestamp, user_id, endpoint, tier):
        pass

Example Configuration
global_limits = {
    "free": (20, 60),
    "premium": (100, 60)
}

Example Usage
limiter = RateLimiter(global_limits, endpoint_limits)

requests = [
    (1, "u1", "/login", "free"),
    (2, "u1", "/login", "free"),
    (3, "u1", "/login", "free"),
    (4, "u1", "/login", "free"),   # blocked
]

Expected Output
True
True
True
False

What This Problem Tests

Clean OOP extensibility

Strategy via configuration

Avoiding tier-specific conditionals

Correct state isolation

Readable, scalable design

Hint (one only)

You already solved this problem twice.
Now you’re just moving limits into dictionaries.

"""
from collections import defaultdict

class RateLimiter:
    def __init__(self, global_limits, endpoint_limits):
        self.global_limits = global_limits
        self.endpoint_limits = endpoint_limits
        self.global_dict = defaultdict(list)
        self.local_dict = defaultdict(lambda:defaultdict(list))


    def allow_request(self, time_stamp, identifier, endpoint, tier):
        
        # global rate limiter

        nums = self.global_dict[identifier]
        

        if tier in self.global_limits:
            limit , window = self.global_limits[tier]
            while nums and time_stamp - nums[0] > window:
                nums.pop(0)
            if len(nums) >= limit:
                return False
            
        
        # local rate limiter

        nums2 = self.local_dict[identifier][endpoint]
        

        if endpoint in self.endpoint_limits[tier]:
            limit1 , window1 = self.global_limits[tier][endpoint]

            while nums2 and time_stamp - nums2[0] > window1:
                nums2.pop(0)
            if len(nums2) >= limit1:
                return False
            nums2.append(time_stamp)

        nums.append(time_stamp)
        return True

    

        







global_limits = {
    "free": (20, 60),
    "premium": (100, 60)
}

endpoint_limits = {
    "free": {
        "/login":  (3, 10),
        "/search": (10, 10)
    },
    "premium": {
        "/login":  (10, 10),
        "/search": (50, 10)
    }
}

limiter = RateLimiter(global_limits, endpoint_limits)

requests = [
    (1, "u1", "/login", "free"),
    (2, "u1", "/login", "free"),
    (3, "u1", "/login", "free"),
    (4, "u1", "/login", "free"),
]

for each in requests:
    print(limiter.allow_request(*each))