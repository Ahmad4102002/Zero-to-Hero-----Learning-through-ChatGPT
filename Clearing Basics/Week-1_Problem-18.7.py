"""
Problem 3 — Smallest Subarray With Sum ≥ S

Given:
An array of positive integers and a number S.
Find the length of the smallest contiguous subarray whose sum ≥ S. If no such subarray exists, return 0.

Example:

nums = [2,3,1,2,4,3]
S = 7
Output: 2  # [4,3]

"""

# IF SUM EXCEEDS 7 MOVE LEFT 


nums = [2,3,1,2,4,3]
s = 7

curr_sum = 0
min_length = 6
left = 0

for r in range(len(nums)):
    curr_sum += nums[r]
    
    while curr_sum >= s:
        w = (r-left)+1
        min_length = min(min_length, w)
        curr_sum -= nums[left]
        left+=1

print(min_length)








