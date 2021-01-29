#!/usr/bin/env python3

def get_middle(s):
	return (s if len(s) < 2 else s[len(s)//2-1:len(s)//2+1] if len(s) % 2 == 0 else s[len(s)//2])
	

print(get_middle("VICTOR"))
