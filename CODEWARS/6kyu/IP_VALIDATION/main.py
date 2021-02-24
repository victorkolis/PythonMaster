#!/usr/bin/env python3

# Validate whether the input is an IP

def is_valid_IP(ip):
	if ''.join(ip.split('.')).isalnum():
		ip = [x for x in ip.split('.')]
		if len(ip) == 4: 
			for element in ip:
				if '0' in element[0] and len(element) > 1:
					return False
				try:
					if int(element) >= 256 or int(element) < 0:
						return False
				except ValueError:
					return False
		else:
			return False
	else:
		return False
	
	return True
	
	
print(is_valid_IP('255.1.0.0'))
