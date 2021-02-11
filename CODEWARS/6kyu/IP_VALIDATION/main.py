#!/usr/bin/env python3

def valid_ip(ip):
	return True if len(ip.split('.')) == 4 and ''.join(ip.split('.')).isnumeric() else False
	
	
print(valid_ip('1.a.0.100'))
