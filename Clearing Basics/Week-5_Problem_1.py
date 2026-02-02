"""
You’re given a list of log entries. Each log entry is a string in the format
"<timestamp> <user_id> <action>"

Example:

logs = [
    "10 alice login",
    "12 bob login",
    "15 alice view",
    "18 alice logout",
    "20 bob view",
    "25 bob logout",
    "30 alice login",
    "35 alice logout"
]


Your task is to write a function analyze_logs(logs) that returns a dictionary with this structure:

{
    "alice": {
        "sessions": 2,
        "actions": 4,
        "active_time": 13
    },
    "bob": {
        "sessions": 1,
        "actions": 3,
        "active_time": 13
    }
}
"""
from collections import defaultdict

class Analyze():
    def __init__(self):
            self.local_dict = defaultdict(lambda: {
            "sessions": 0,
            "actions": 0,
            "active_time": 0,
            "last_login": None
        })
    
    def analyze_logs(self,time_stamp, user_id, action):
        time_stamp = int(time_stamp)
        self.local_dict[user_id]["actions"] += 1

        if action == "login":
            self.local_dict[user_id]["sessions"] += 1
            self.local_dict[user_id]["last_login"] = time_stamp
        
        elif action == "logout":
            login_time = self.local_dict[user_id]["last_login"]
            if login_time is not None:
                self.local_dict[user_id]["active_time"] += time_stamp - login_time
                self.local_dict[user_id]["last_login"] = None
        
logs = [
    "10 alice login",
    "12 bob login",
    "15 alice view",
    "18 alice logout",
    "20 bob view",
    "25 bob logout",
    "30 alice login",
    "35 alice logout"
]
analyzer = Analyze()

for each in logs:
    each = each.split()
    analyzer.analyze_logs(*each)