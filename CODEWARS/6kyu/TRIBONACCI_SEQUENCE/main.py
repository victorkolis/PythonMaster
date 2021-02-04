#!/usr/bin/env python3

def tribonacci(signature, n):
	if n == 1:
		return [signature[0]]
	elif n == 0:
		return []
	elif n == 2:
		return signature[:2]
	elif n == 3:
		return signature[:3]
	
	for index in range(n):
		try:
			signature += [signature[index] + signature[index + 1] + signature[index + 2]]
			if len(signature) == n:
				break
		except IndexError:
			pass
	return signature


print(tribonacci([1, 1, 1], 1))
