import time

def fibonacci(n, a=0, b=1):	#Returns nth number, index starting at 1, of fibonacci sequence starting with a,b.
	startTime = time.time()
	i = 1
	c = b			#Handles case n = 1 or n = 2.
	if n == 1:
		return a
	while i <= (n-2):
		c = a + b
		a = b
		b = c
		i += 1
	print("- %s seconds -" % (time.time() - startTime))
	return c

def fibonacciB(n, a=0, b=1):	#Returns nth number, index starting at 1, of fibonacci sequence starting with a,b.
	startTime = time.time()
	i = 1		#Handles case n = 1 or n = 2.
	if n == 1:
		return a
	while i <= (n-2):
		a, b = b, a+b
		i += 1
	print("- %s seconds -" % (time.time() - startTime))
	return b

fibonacci(1000000, 1, 2)
#fibonacciB(2000000, 1, 2)
	
