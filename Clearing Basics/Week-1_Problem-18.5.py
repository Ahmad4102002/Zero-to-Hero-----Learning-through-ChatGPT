"""
Problem 3 — Maximum Subarray Length With Sum ≤ K

Given:

An array of positive integers nums

An integer k representing a maximum sum

Task:
Find the length of the longest contiguous subarray whose sum is less than or equal to k.

Return the length of this subarray.

Input

nums: List of positive integers

k: Positive integer

Output

Single integer: maximum length of any contiguous subarray with sum ≤ k

Example
nums = [2, 1, 5, 1, 3, 2]
k = 7


Valid subarrays whose sum ≤ 7:

[2,1] → sum = 3 → length = 2

[1,5,1] → sum = 7 → length = 3

[5,1] → sum = 6 → length = 2

[1,3,2] → sum = 6 → length = 3

Answer: 3

Constraints / Mental Model

All numbers are positive, which guarantees that if the sum exceeds k, you can safely shrink the window from the left.

Use a variable-size sliding window:

Expand the window to the right as long as sum ≤ k

Shrink the window from the left if sum > k

Update the maximum length each step

Brute force: O(n²) → sliding window: O(n)
"""


nums = [2, 1, 5, 1, 3, 2]

k = 7

left = 0 
curr_sum = 0
length = 0 

n = len(nums)

for r in range(n):
    curr_sum += nums[r]
    while curr_sum > k:
        curr_sum -= nums[left]
        left += 1
    
    w = (r - left) + 1
    length = max(length, w)
print(length)
