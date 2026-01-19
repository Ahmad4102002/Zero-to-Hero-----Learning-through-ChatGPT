"""
Problem 2 — Longest Subarray With Ones After Flipping Zeros

Given:
An array of 0s and 1s, and an integer k representing the maximum number of 0s you can flip to 1.
Find the length of the longest contiguous subarray of 1s you can obtain by flipping at most k zeros.

Example:

nums = [1,0,1,1,0,1,0,1]
k = 2
Output: 6  # flip two 0s in the middle
"""

nums = [1,0,1,1,0,1,0,1]

k = 2

length = 0
left = 0
zero_count = 0

for r in range(len(nums)):
    if nums[r] == 0:
        zero_count += 1
    while zero_count > k:
        if nums[left] == 0:
            zero_count -=1
        left+=1
    w = (r-left) + 1
    length = max(length,w)
print(length)




    


# length of longest 11 string





