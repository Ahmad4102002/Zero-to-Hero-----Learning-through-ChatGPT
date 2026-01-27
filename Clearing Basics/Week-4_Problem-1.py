"""
You are building a production-grade API rate limiter.

Each incoming request has:

timestamp (integer, seconds)

user_id (string)

endpoint (string)

Rate-Limiting Rules
1. Global Limit (per user)

A user can make at most 20 requests in any 60-second window,
across all endpoints combined.

2. Endpoint Limit (per user per endpoint)

Each endpoint has its own rate-limit rules:

Example configuration:

endpoint_limits = {
    "/login":  (3, 10),
    "/search": (10, 10),
    "/upload": (1, 60)
}


Meaning:

/login → max 3 requests per 10 seconds

/search → max 10 requests per 10 seconds

/upload → max 1 request per 60 seconds

Important Behavior Rules

Global limit is checked first

If a request is blocked globally, it must NOT affect endpoint counts

If a request is blocked locally, it must NOT affect global counts

Blocked requests are never stored

Old timestamps must be cleaned before checking limits

Class Design (Must Use This)
class RateLimiter:
    def __init__(self, global_limit, global_window, endpoint_limits):
        pass

    def allow_request(self, timestamp, user_id, endpoint):
        pass

Example Usage
limiter = RateLimiter(
    global_limit=20,
    global_window=60,
    endpoint_limits={
        "/login":  (3, 10),
        "/search": (10, 10),
        "/upload": (1, 60)
    }
)

requests = [
    (1, "u1", "/login"),
    (2, "u1", "/login"),
    (3, "u1", "/login"),
    (4, "u1", "/login"),   # blocked locally
]

Expected Output
True
True
True
False

Constraints

Use only Python standard library

Use sliding window logic

Time complexity per request must be O(1) amortized

No global variables

Clean, readable code matters

"""
from collections import defaultdict

class RateLimiter:
    def __init__(self,global_limit,global_window,endpoint_limits):
        
        self.global_limit = global_limit
        self.global_window = global_window
        self.endpoint_limits = endpoint_limits
        self.global_dict = defaultdict(list)
        self.local_dict = defaultdict(lambda: defaultdict(list))

    def allow_request(self,time_stamp,identifier,endpoint):

        # global rate limiter : A user can make at most 20 requests in any 60-second window, across all endpoints combined.
        nums = self.global_dict[identifier]
        while nums and time_stamp - nums[0] > self.global_window:
            nums.pop(0)
        if len(nums) >= self.global_limit:
            return False
        

        #local rate limiter : Endpoint Limit (per user per endpoint) Each endpoint has its own rate-limit rules

        if endpoint in self.endpoint_limits:
            limit, window = self.endpoint_limits[endpoint]
            nums2 = self.local_dict[identifier][endpoint]

            while nums2 and time_stamp - nums2[0] > window:
                nums2.pop(0)
            if len(nums2) >= limit:
                return False
            nums2.append(time_stamp)
        
        nums.append(time_stamp)
        return True
        
limiter = RateLimiter(
    global_limit=20,
    global_window=60,
    endpoint_limits={
        "/login":  (3, 10),
        "/search": (10, 10),
        "/upload": (1, 60)
    }
)

requests = [
    (1, "u1", "/login"),
    (2, "u1", "/login"),
    (3, "u1", "/login"),
    (4, "u1", "/login"),
]
for each in requests:
    print(limiter.allow_request(*each))

