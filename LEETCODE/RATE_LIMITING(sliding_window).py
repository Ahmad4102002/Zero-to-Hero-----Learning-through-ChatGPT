
"""
# If more than 5 requests hit the same endpoint from the same IP within any 10-second window, mark it as "RATE_LIMITED", otherwise "OK"

{'count': 6, 'last_access': [1, 2, 3, 4, 5, 6]}
                            [1, 2]
                            [1, 2, 3]
                            [1, 2, 3, 4]
                            [1, 2, 3, 4, 5]         # WATCH SLIDING WINDOW LOGIC ON YOUTUBE SO I CAN COVER EACH PATTERN EFFECIENTLY
                            [1, 2, 3, 4, 5, 6]
                            [2, 3, 4, 5, 6]
                            [2, 3, 4, 5, 6]
# step 1 how many less and eueal to 10 second window exit(SLIDING WINDOW)
# step 2 if count of hits (ie [1,2,3,4,5] is 5 ) is greater than 5 then RATELIMITED (I HAVE To EXIT THE LOOP ON FIRST OCCURANCE OF >5 AND SET VALUE TO RATELIMITED)

# in [1,2,3,4,5] if the last index 5(represents 5 second window) 
# get count of [1,2,3,4,5]



{'count': 1, 'last_access': [2]}
# step 1 how many less or eual to 10 secondwindow exist
# step 2 if count of hits (ie [2]is 1 ) is greater than 5 then 

{'count': 2, 'last_access': [1, 20]}
@                 @                     @
. . . . . . . . . . . . . . . . . . . . .
*                                       *
# IF LAST _ FIRSST > 10 NOT WITHIN
"""
dik = [2, 24]
lic = []

a = max(dik)

for i in range(a):
    if i + 1 in dik:
        #print("*", end=" ")
        lic.append("*")
    else:
        #print(".", end=" ")
        lic.append(".")
#print(" ")
print(lic)

#create 10 second windows
#then create if condition that if count of * is greater than 5 then print (change dictionary)


# lic = ['.', '*', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*']

for i in range(len(lic)):
    print(i , end=" ")

