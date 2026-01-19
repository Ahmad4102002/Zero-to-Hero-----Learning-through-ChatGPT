nums = [1, 2, 3, 4, 5, 20]

# If more than 5 requests hit the same endpoint from within any 10-second window, mark it as "RATE_LIMITED"

left = 0 

w = 0 

for r in range(len(nums)):
    w = (r-left) + 1 

    while nums[r] - nums[left] > 10:     
        left +=1  
        if w > 5:
            print("RATE_LIMITED")

        
    
