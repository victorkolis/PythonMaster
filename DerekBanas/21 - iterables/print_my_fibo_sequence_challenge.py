#!/usr/bin/env python3

# Sample Output
# Fib : 1
# Fib : 2
# Fib : 3
# Creating a class that returns the Fib sequence


class FibSequence:
	def __init__(self):
		self.first = 0
		self.second = 1
		
	def __iter__(self):
		return self
	
	def __next__(self):
		fib_num = self.first + self.second
		self.first = self.second
		self.second = fib_num
		return fib_num

	

fib = FibSequence()

for _ in range(10):
	print('Fib:', next(fib))
