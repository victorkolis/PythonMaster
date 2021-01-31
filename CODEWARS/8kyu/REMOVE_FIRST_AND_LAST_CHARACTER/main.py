#!/usr/bin/env python3

# Love -> ov

def remove_char(s):
	return '' if len(s) <= 2 else s[1:len(s)-1]

print(remove_char('mem'))
