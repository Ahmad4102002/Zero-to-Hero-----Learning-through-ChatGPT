"""

nums = [1, 2, 1, 3, 2, 1, 4, 3, 2]
Build:

yaml
Copy code
{
  "odd":  {1: 3, 3: 2},
  "even": {2: 3, 4: 1}
}
New Rule
• You may not write:

python
Copy code
if key not in dict:
You must use exactly one loop.
"""

from collections import defaultdict

nums = [1, 2, 1, 3, 2, 1, 4, 3, 2]
dih = defaultdict(lambda:(defaultdict(int)))

for each in nums:
    key = "odd" if each % 2 == 1 else "even"
    dih[key][each] += 1

print(dih)

    