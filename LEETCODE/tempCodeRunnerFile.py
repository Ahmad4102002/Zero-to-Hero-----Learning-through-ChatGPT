times = [1, 2, 3, 4, 5, 6, 20]

left = 0 

for right in range(len(times)):
   
    while times[right]-times[left] > 10:
        left +=1
    if  (right-left) + 1:
        print("RATE_LIMITED")
    