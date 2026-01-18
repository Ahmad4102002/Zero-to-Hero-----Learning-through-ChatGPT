times = [1, 2, 3, 4, 5, 6, 20]

left = 0 

for right in range(len(times)):
   # 1 - 0 !>10 so right will increase as it is the pointer tha moves with the loop \

    while times[right]-times[left] > 10:
        #left = 1
        left +=1
    if  (right-left + 1)>= 6:
        print("RATE_LIMITED")
    else:
        print("OK")
    