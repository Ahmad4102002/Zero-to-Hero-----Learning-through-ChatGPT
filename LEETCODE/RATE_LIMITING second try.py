"""1, 2, 3, 4, 5, 6, 20

The rule in plain English is:

“Did this user make more than 5 requests within 10 seconds?”

That means you are not asking:
“Is the last access ≤ 10?”
“Is the count > 5?”

Those are shortcuts — and they break.

You are asking:
“Is there any group of 6 requests where the time difference between the first and last is ≤ 10?”


minimum substring length 6
time difference 


x++

x to x+5
"""

liss = [1, 2, 3, 4, 5, 6, 20]

print(new)