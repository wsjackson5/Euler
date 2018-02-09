a = 1234

def circ(i):				#return circulars of a number, in a list
	j = str(i)
	n = (len(j) - 1)
	k = 0
	circs = []
	while k <= n:
		x = j[k:]+j[:k]
		circs.append(int(x))
		k += 1
	return circs

some_map = circ(a)
print(some_map)

required_values = [1234, 2341, 3412, 4123, 5678]


print(all(x in required_values for x in some_map))

#create a bool list for primes list. for each prime run circ, then check against prime list, if true mark the
#bool for that prime as true. compress the lists, and len()
