"""
Calculate Factorial in Python
"""

import math

def factorial(n):
	"Method to calcualte factorial"
	if not isinstance(n,int):
		print '\nFactor is only defined for integers.'
		return -1
	else:
		if n == 0:
			return 1
		else:
			return  n * factorial(n-1)

x = 910 # you can change this number, 90, to your own.
print ('Factorial of ', x , ' is ', factorial(x))