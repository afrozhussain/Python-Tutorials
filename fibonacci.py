"""
Print Fibonacci Series 
"""

import math

def fibonacci(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

# Print first 10 fibonacci numers
limit = 10

for i in range(limit):
	
	print (fibonacci(i))
	
	
	