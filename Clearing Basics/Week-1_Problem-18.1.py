"""
Level 1 — Window Size Basics (no shrinking logic)
Problem 1: Max Sum of Fixed Window

Given a list and k, find the maximum sum of any subarray of size k.

Example:

nums = [2, 1, 5, 1, 3, 2]
k = 3


Expected:

9   # subarray [5,1,3]


Rules:
• One loop
• No nested loops
• Must use sliding window

Focus:
➡️ Understanding fixed-size windows

"""

nums = [2, 1, 5, 1, 3, 2]
k = 3
n = len(nums)
curr_sum = 0

for i in range(k):
    curr_sum += nums[i]

max_sum = curr_sum

for i in range(k,n):
    curr_sum += nums[i]
    curr_sum -= nums[i-k]

    if curr_sum > max_sum :
        max_sum = curr_sum

print(max_sum)