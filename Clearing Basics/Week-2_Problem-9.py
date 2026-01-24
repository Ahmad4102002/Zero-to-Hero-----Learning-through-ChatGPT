"""
Week – 2
Problem – 3: Sliding Window Error Spike Detection

You are given a stream of server logs represented as tuples:

(timestamp, status_code)

Where:

timestamp is an integer representing time in seconds (strictly increasing)

status_code can be 200 (success) or 500 (error)

Objective:
Detect abnormal error spikes using a sliding window technique.

Rule:
If more than 3 error responses (500) occur within any 20-second window, return "ALERT" for that request. Otherwise, return "OK".

Important Notes:

The check must be done for every incoming log entry

Use an efficient sliding window approach

Do not recompute the window from scratch for each log

Once an error triggers "ALERT", it should still remain part of future windows

Input Example:

logs = [
    (1, 200),
    (5, 500),
    (7, 500),
    (10, 200),
    (12, 500),
    (15, 500),
    (18, 200),
    (22, 500)
]


Expected Output Format:
For each log entry, print either:

OK
ALERT


Function Signature:

def detect_error_spike(logs):
    pass

"""


def detect_error_spike(logs):
    left = 0
    error = 0
    
    

    for right in range(len(logs)):
        time_stamp = logs[right][0]
        codes = logs[right][1]

        if codes == 500:
            error += 1
        while time_stamp - logs[left][0] > 20:
            if logs[left][1] == 500:
                error -= 1
            left+=1
        if error > 3:
            print("ALERT") 
        else:
            print("OK")




logs = [
    (1, 200),
    (5, 500),
    (7, 500),
    (10, 200),
    (12, 500),
    (15, 500),
    (18, 200),
    (22, 500)
]

detect_error_spike(logs)




