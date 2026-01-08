



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
 
