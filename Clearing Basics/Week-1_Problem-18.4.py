"""
Given an array of integers nums, an integer k, and a number x, determine whether there exists a contiguous subarray of size k whose average is greater than or equal to x.

Return True if such a subarray exists, otherwise return False.

Constraints

1 ≤ k ≤ len(nums)

nums contains integers (positive, negative, or zero)

Example

nums = [2, 1, 5, 1, 3, 2]
k = 3
x = 3
Output: True

"""

nums = [2, 1, 5, 1, 3, 2]
k = 3
x = 3

n = len(nums)

curr_sum = 0
avg = 0

for i in range(k):
    curr_sum += nums[i]
avg = curr_sum / k
if avg >= x:
    print("True")

for i in range(k,n):
    curr_sum += nums[i]
    curr_sum -= nums[i-k]

    avg = curr_sum / k

    if avg >= x:
        print("True")
        break




