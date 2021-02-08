#!/usr/bin/env python3

# tail, body, head -> head, body, tail

def fix_the_meerkat1(arr):
	return arr[::-1]

# or
def fix_the_meerkat2(arr):
	return list(reversed(arr))


print(fix_the_meerkat1(['tail', 'body', 'head']))
print(fix_the_meerkat2(['tail', 'body', 'head']))
