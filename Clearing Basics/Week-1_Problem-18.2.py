"""
Find the longest subarray with sum ≤ 7

nums = [2, 1, 5, 1, 3, 2]
k = 7


This one requires while, and once you solve it, the rate-limit logic will feel obvious.

"""

nums = [2, 1, 5, 1, 3, 2]
k = 7

left = 0
longest = 0
curr_sum = 0

for i in range(len(nums)):
    curr_sum += nums[i]
    while curr_sum > 7:
        curr_sum -= nums[left]
        left += 1
    
    w = (i-left) + 1

    longest = max(longest,w)

print(longest)

    


