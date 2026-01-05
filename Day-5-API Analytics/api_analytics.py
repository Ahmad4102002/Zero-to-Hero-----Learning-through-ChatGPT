
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

def reuests_per_status():
    codes = {}

    for each in liss:
        ip = each[3]
        codes[ip] = codes.get(ip, 0) + 1

    return codes

def status_codes_per_endpoint():
    sc_endpoints = {}

    for each in liss:

        ep = each[2]
        sc = each[3]

        if ep not in sc_endpoints:
            sc_endpoints[ep] = {}


        sc_endpoints[ep][sc] = sc_endpoints[ep].get(sc, 0) + 1

    return sc_endpoints

def most_accessed_endpoint():

    ep = reuests_per_endpoint()
    max_endpoint = max(ep,key = ep.get)
    print(f"The most accessed endpoint is {max_endpoint} accessed {ep[max_endpoint]} times")

def most_accessed_ip():

    ep = reuests_per_ip()
    max_endpoint = max(ep,key = ep.get)
    print(f"The most active ip is {max_endpoint} accessed {ep[max_endpoint]} times")

def failed_reuests():
    count = 0

    for each in liss:
        status_code = int(each[4])

        if status_code // 100 == 4 or status_code // 100 == 5:
            count += 1

    print(f"The number of failed requests is: {count}")

def avg_respons_per_endpoint():

    response = {}

    for each in liss:
        endpoint = each[2]
    
        if endpoint not in response:
           response[endpoint] = []
    
        response[endpoint].append(int(each[5]))
    
    for every in response:
        response[every] = int(sum(response[every])/ len(response[every]))
    
    print(response)

    #for each in liss:
    #   response[each[2]] = response.get(each[2], 0) + int(each[5])
    # print(response)
        
    

def main():

    print("EXIT - 1")
    print("Total number of reuests - 2")
    print("Reuests made per endpoint - 3")
    print("Reuests made per ip - 4")
    print("Most accessed endpoint - 5")
    print("Most active ip - 6")
    print("reuests made per status code - 7")
    print("status codes per endpoint - 8 ")
    print("Total number of reuests failed - 9")
    print("Average response per endpoint - 10")
    
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
    
    if n == 7:
        print(reuests_per_status())
        return True
    
    if n == 8:
        print(status_codes_per_endpoint())
        return True
    
    if n == 9:
        failed_reuests()
        return True
    
    if n == 10:
        avg_respons_per_endpoint()
        return True
    


if __name__ == "__main__":

    liss = []
    with open("Day-5-API Analytics\\api_logs.txt","r") as file:
        for line in file:
            liss.append(line.split())
    while True:
        if not main():
            break



