s = "abcabcbb"

# find length of the logest substring where digits do not repeat

l = 0 
longest = 0 

sett =set()

n = len(s)

for r in range(n):
    while s[r] in sett:
        sett.remove(s[l])
        l += 1

    w = (r-l) + 1
    longest = max(longest, w )
    sett.add(s[r])

print(longest)
print()

