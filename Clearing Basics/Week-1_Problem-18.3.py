"""
Problem 1 — Maximum Sum Subarray of Size K

You are given an array of positive integers nums and an integer k.

Return the maximum sum of any contiguous subarray of size k.

Example
Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: Subarray [5,1,3] has the maximum sum.

"""

nums = [2, 1, 5, 1, 3, 2]

k = 3

curr_sum = 0

n = len(nums)

for i in range(k):
    curr_sum += nums[i]

max_sum = curr_sum

for i in range(k,n):
    curr_sum += nums[i]
    curr_sum -= nums[i-k]

    if curr_sum > max_sum:
        max_sum = curr_sum

print(max_sum)
