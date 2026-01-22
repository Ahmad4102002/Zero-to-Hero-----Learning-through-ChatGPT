"""
Day 7 – Problem 1: API request deduplication (logic only)
Problem statement

You are building a backend service that receives requests with an idempotency key.

Each request is:

(request_id, timestamp_in_seconds)


Rules:

• If the same request_id is received again within 30 seconds, it must be treated as DUPLICATE
• If it arrives after 30 seconds, it is treated as a NEW request
• Requests arrive in time order

Input
requests = [
    ("abc", 1),
    ("xyz", 5),
    ("abc", 10),
    ("abc", 35),
    ("xyz", 36),
    ("xyz", 60)
]

Expected output (important)

For each incoming request, immediately print:

(request_id, "NEW" or "DUPLICATE")


Expected prints:

("abc", "NEW")
("xyz", "NEW")
("abc", "DUPLICATE")
("abc", "NEW")
("xyz", "NEW")
("xyz", "DUPLICATE")

Constraints / Intent (read carefully)

• This is online processing (one request at a time)
• You must store minimal state
• Old request IDs must be evicted once they are no longer relevant
• This is not a batch problem

What I expect you to do

1️⃣ Decide what data structure you need
2️⃣ Decide when old entries should be removed
3️⃣ Write a handle_request(request_id, timestamp) function
4️⃣ Simulate incoming requests by looping over requests
"""

dih = {}
def handle_reuests(id, time_stamp):

    if id not in dih:
        print(f"{id} : NEW ")
        dih[id] = time_stamp
        return

    if time_stamp - dih[id]  < 30:
        print(f"{id} : DUPLICATE")
    else:
        print(f"{id} : NEW ")
    
    dih[id] = time_stamp

requests = [
    ("abc", 1),
    ("xyz", 5),
    ("abc", 10),
    ("abc", 35),
    ("xyz", 36),
    ("xyz", 60)
]



for log in requests:
    handle_reuests(*log)