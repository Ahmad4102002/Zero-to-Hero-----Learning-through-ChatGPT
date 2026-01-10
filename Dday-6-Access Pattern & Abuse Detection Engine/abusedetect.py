
def total_reuests():
    return len(events)

def reuests_per_endpoint():

    reuests = {}

    for each in events:
        reuests[each["endpoint"]] = reuests.get(each["endpoint"], 0) + 1
    
    return reuests

def reuests_per_ip():

    reuests = {}

    for each in events:
        reuests[each["ip"]] = reuests.get(each["ip"], 0) + 1
    
    return reuests

def reuests_per_status():

    reuests = {}

    for each in events:
        reuests[each["status"]] = reuests.get(each["status"], 0) + 1
    
    return reuests

def status_codes_per_endpoint():

    status_codes = {}

    for each in events:

        if each["endpoint"] not in status_codes:
            status_codes[each["endpoint"]] = {}
        status_codes[each["endpoint"]][each["status"]] = status_codes[each["endpoint"]].get(each["status"] , 0) + 1 
    
    return status_codes

def count_failed():

    failed = []

    for each in events:
        if each["status"] // 100 == 4 or each["status"] //100 == 5:
            failed.append(each)
    
    return len(failed)

def most_accessed_endpoint():
    a = reuests_per_endpoint()

    most_accessed = max(a, key = a.get)

    return most_accessed

def avg_response_times_per_endpoint():
    response_times = {}

    for each in events:

        if each["endpoint"] not in response_times:
           response_times[each["endpoint"]] = []

        response_times[each["endpoint"]].append(int(each["response"])) 

    for every in response_times:
        response_times[every] = int(sum(response_times[every])/len(response_times[every]))
    

    return response_times

def most_reuests_per_hour():

    reuests = {}

    for each in events:
        reuests[each["hour"]] = reuests.get(each["hour"], 0) + 1

    max_time = max(reuests, key = reuests.get)
    
    return max_time

def main():

    print("EXIT - 1")
    print("Total number of reuests - 2")
    print("Reuests per Endpoint - 3")
    print("Reuests per ip - 4")
    print("Reuests per status code - 5")
    print("Status codes per endpoint - 6")
    print("Total number of failed reuests - 7")
    print("Most accessed endpoint - 8")
    print("Average Response time per endpoint - 9")
    print("Peak traffic hours - 10")


    try:
        n = int(input().strip())
    except ValueError :
        print("Enter Correct Number")
        return True 


    if n == 1:
        print("------------Exited gracefully------------")
        return False
    
    if n == 2:
        print(f"The total number of reuests is : {total_reuests()}")
        return True
    
    if n == 3:
        print(reuests_per_endpoint())
        return True
    
    if n == 4:
        print(reuests_per_ip())
        return True
    
    if n == 5:
        print(reuests_per_status())
        return True
    
    if n == 6:
        print(status_codes_per_endpoint())
        return True
    
    if n == 7:
        print(count_failed())
        return True
    
    if n == 8:
        print(f"The most accessed endpoint is : {most_accessed_endpoint()}")
        return True
    
    if n == 9:
        print(avg_response_times_per_endpoint())
        return True
    
    if n == 10:
        print(f"Peak hour is : {most_reuests_per_hour()}")
        return True
    

if __name__ == "__main__":
    events =[]
    with open("Dday-6-Access Pattern & Abuse Detection Engine\\api_logs.txt", "r") as file:
        for line in file:
            parts = line.split()
            
            timestamp = parts[0]
            ip        = parts[1]
            endpoint  = parts[2]
            method    = parts[3]
            status    = int(parts[4])
            response  = int(parts[5])

            hour = int(timestamp.split("T")[1].split(":")[0])

            event = {
                        "timestamp": timestamp,
                        "hour": hour,
                        "ip": ip,
                        "endpoint": endpoint,
                        "method": method,
                        "status": status,
                        "response": response
                    }  
            
            events.append(event)
    while True:
        if not main():
            break
 
