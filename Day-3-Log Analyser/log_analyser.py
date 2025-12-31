ip_address = {}
endpoints = {}
statuscodes = {}


def count_ip():
    
    for each in line2:
        ip = each[0]
        ip_address[ip] = ip_address.get(ip, 0) +1

    print(ip_address)
 

def count_endpoint():
    
    for each in line2:
        end = each[2]
        endpoints [end] = endpoints.get(end, 0) +1

    print(endpoints)

def count_status_codes():

    for each in line2:
        stat = each[3]
        statuscodes[stat] = statuscodes.get(stat, 0) +1

    print(statuscodes)
        

def max_fre_ip():

    count_ip()
    max_ip = max(ip_address, key=ip_address.get)
    print(max_ip, ip_address[max_ip])

def max_end():

    count_endpoint()
    max_endp = max(endpoints, key = endpoints.get)
    print(max_endp, endpoints[max_endp])


def main():
        
    print("count freuency of IP addresses - 1 ")
    print("count freuency of endpoints - 2 ")
    print("find max ip produced - 3 ")
    print("find max endpoints - 4")
    print("count status codes - 5")

    n = int(input().strip())
    
    if n == 1:
        count_ip()
    
    if n == 2:
        count_endpoint()

    if n == 3:
        max_fre_ip()

    if n == 4:
        max_end()
    if n == 5:
        count_status_codes()

    

if __name__ == "__main__":
    line2 = []
    with open("Log Analyser\server.log", "r") as file:
        for line in file:
            line = line.split()

            if not line:
                continue

            line2.append(line)
        print(line2)

    while True:
        main()

