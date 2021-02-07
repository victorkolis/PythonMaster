#!/usr/bin/env python3

# receive 2 IPv4 addresses and return the difference betwixt them

def ips_between(ip1, ip2):
	
	ip1 = [int(x) for x in ip1.split('.')][::-1]
	ip2 = [int(x) for x in ip2.split('.')][::-1]
	
	for index, element in enumerate(ip1):
		ip1[index] = element + (255 * index)
		
	for index, element in enumerate(ip1):
		ip2[index] = element + (255 * index)
	return abs(sum(ip1) - sum(ip2))


print(ips_between("10.0.0.0", "10.0.1.0"))
