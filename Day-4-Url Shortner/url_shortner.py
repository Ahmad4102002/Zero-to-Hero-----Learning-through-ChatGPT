def url_count():

    global url_counts
    url_counts = {}

    for every in liss:
            url_counts[every[1]] = url_counts.get(every[1], 0) + 1
    print(url_counts)

def max_url():
     url_count()
     max_url = max(url_counts,key = url_counts.get)
     print(max_url,url_counts[max_url])

def uni_ip_url():

    global uni
    uni = {}

    for every in liss:
          
        if every[2] not  in uni:
            uni[every[2]] = {}

        uni[every[2]][every[1]] = uni[every[2]].get(every[1],0 ) +1
    
    print(uni)

def failed_re():

    global fail_pass
    fail_pass = {}

    for each in liss:
        fail_pass[each[3]] = fail_pass.get(each[3], 0) + 1
    
    print(fail_pass["FAIL"])

def status_codes_url():

    global status_codes
    status_codes = {}

    
    for every in liss:
        
        if every[1] not in status_codes:
            status_codes[every[1]] = {}

        status_codes[every[1]][every[3]] = status_codes[every[1]].get(every[3], 0) +1

    print(status_codes)
    
    


def reuest_count_ip():

    global ips
    ips = {}

    for each in liss:
        ips[each[2]] = ips.get(each[2], 0) + 1

def max_reuests_count():
    reuest_count_ip()

    max_ip = max(ips, key = ips.get)
    print(max_ip,ips[max_ip])


def final_report_url():
   
    print("Enter URL name : ")
    b = input().strip()
    
    url_count()
    uni_ip_url()
    failed_re()
    status_codes_url()

    print("-------------------------------------------------")
    
    print(f"{b} has be accessed {url_counts[b]} times ")

    count = 0
    for value in uni.values():
        
        if b in value:
            count += 1
        
    print(f"{b} has been accesed {count} uniue times")

    
    for key,valu in uni.items():
        
        if b in valu:
            print(f"{key} ip accessed {b} url  {valu[b]} times")
    

    if b in status_codes:
        print(b , status_codes[b])



def main():
    print("count Url accessed - 1")
    print("max url accessed - 2")
    print("uniue ip and count of url accessed - 3")
    print("How many failed - 4")
    print("Max reuest per ip  - 5")
    print("Print Report for URL - 6")

    n = int(input().strip())

    if n == 1:
        url_count()
    
    if n == 2:
        max_url()
    
    if n == 3:
        uni_ip_url()

    if n == 4:
        failed_re()

    if n == 5:
        max_reuests_count()

    if n == 6:
        final_report_url()



if __name__ == "__main__":
    liss = []
    with open("Day-4-Url Shortner\\url_logs.txt", "r") as file:
        for line in file:
            liss.append(line.split())
    while True:
        main()

    

        
    
