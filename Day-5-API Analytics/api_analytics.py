
def total_reuests():

    print(f"The count of reuests is : {len(liss)}")

def reuests_per_endpoint():
    endpoints = {}

    for each in liss:
        endpoint = each[2]
        endpoints[endpoint] = endpoints.get(endpoint, 0) + 1

    return endpoints

def reuests_per_ip():
    ips = {}

    for each in liss:
        ip = each[1]
        ips[ip] = ips.get(ip, 0) + 1

    return ips
    
def most_accessed_endpoint():

    ep = reuests_per_endpoint()
    max_endpoint = max(ep,key = ep.get)
    print(f"The most accessed endpoint is {max_endpoint} accessed {ep[max_endpoint]} times")

def most_accessed_ip():

    ep = reuests_per_ip()
    max_endpoint = max(ep,key = ep.get)
    print(f"The most active ip is {max_endpoint} accessed {ep[max_endpoint]} times")

def main():

    print("EXIT - 1")
    print("Total number of reuests - 2")
    print("Reuests made per endpoint - 3")
    print("Reuests made per ip - 4")
    print("Most accessed endpoint - 5")
    print("Most active ip - 6")

    n = int(input().strip())

    if n == 1:
        return False 
    if n == 2:
        total_reuests()
        return True
    
    if n == 3:
        print(reuests_per_endpoint())
        return True
    
    if n == 4:
        print(reuests_per_ip())
        return True

    if n == 5:
        most_accessed_endpoint()
        return True
    
    if n == 6:
        most_accessed_ip()
        return True
    


if __name__ == "__main__":

    liss = []
    with open("Day-5-API Analytics\\api_logs.txt","r") as file:
        for line in file:
            liss.append(line.split())
    print(liss)
    while True:
        if not main():
            break



