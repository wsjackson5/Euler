def fibonacci(n, a=0, b=1):	#Returns nth number, index starting at 1, of fibonacci sequence starting with a,b.
	i = 1
	c = b			#Handles case n = 1 or n = 2.
	if n == 1:
		return a
	while i <= (n-2):
		c = a + b
		a = b
		b = c
		i += 1
	return c

print(fibonacci(1000, 1, 2))
		
