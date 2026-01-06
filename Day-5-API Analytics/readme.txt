The Reuirements given to me by ChatGPT

Core Features 

The system must support the following analytics:

Total number of API requests
Number of requests per endpoint
Number of requests per IP address
Most accessed API endpoint
Most active IP address
Count of requests per HTTP status code
Status code distribution per endpoint
Number of failed requests (4xx and 5xx)
Average response time per endpoint
Slowest API endpoint (highest average response time)

total_reuests() : Counts total reuests made

reuests_per_endpoint() : Creates a dictionary endpoints. Saves the endpoint names and their count.

reuests_per_ip() : Creates a dictionary ips . Saves the ip names and their count.

reuests_per_status() : Creates  a dictionary codes. Saves the status code names and their count.

status_codes_per_endpoint() : Creates a dictionary sc_endpoints. This disctionary is a nested dictionary with enpoints as out keys
                              and status codes returned as inner keys.

most_accesed_endpoint() : calls the reuests_per_endpoint() funstion asnd stores the value in a variable and finds the max value and 
                          corresponding value.

most_accesed_ip() :       calls the reuests_per_ip() funstion asnd stores the value in a variable and finds the max value and 
                          corresponding value.

failed_reuests() : checks for status codes starting with 4 and 5 by diving the codes with 100 and stores their counts.

avg_response_per_endpoint() : Creates a nested dictionary response. First the dictionary stores endpoint names as outer keys and their corresponding 
                              response times in a vlue list. Then the value list is replaced by their average response time.

max_avg_response_per_endpoint() : calls avg_respons_per_endpoint() and find the max value.



