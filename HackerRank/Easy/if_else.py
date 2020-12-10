#!/usr/bin/env python3

"""
Task -
Given an integer, perform the following conditional actions:
If is odd, print Weird. If is even and in the inclusive range of to,
print Not Weird. If is even and in the inclusive range of to, print Weird.
If is even and greater than, print Not Weird

Input Format:
A single line containing a positive integer,

Constraints:
1 <= n <= 100

Output Format:
Print Weird if the number is weird. Otherwise, print Not Weird.
"""

n = int(input('Enter a number: '))

# All Weirds
if not n % 2 == 0:
    print('Weird')
elif n % 2 == 0 and 5 < n <= 20:
    print('Weird')

# All Not Weirds
elif n % 2 == 0 and n < 5:
    print('Not Weird')
elif n % 2 == 0 and n > 20:
    print('Not Weird')
