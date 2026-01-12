"""
nums = [1, 2, 1, 3, 2, 1, 4, 3, 2]
Count only numbers greater than 2.

So:
– 1 and 2 must not appear at all
– 3 and 4 must be counted
– dictionary is built during the loop

Before you code, say this sentence to yourself:

“On each iteration, I either ignore the number or update the dictionary.”"""

nums = [1, 2, 1, 3, 2, 1, 4, 3, 2]

greater = {}

for each in nums:
    if each > 2:
        greater[each] = greater.get(each, 0) +1

print(greater)