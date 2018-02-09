from itertools import compress
import time
from multiprocessing import Pool

def getPrimes(start, end):
	startTime = time.time()
	num = [x for x in range (start, end)]
	bools = [True] * (end - start)
	for i in num:
		if (i >= 2):	
			if bools[i] == True:
				j = 2
				while ((i * j) < end):
					bools[i * j] = False
					j += 1

	bools[0] = False
	bools[1] = False
	primes = list(compress(num, bools))
	
	print("- %s seconds -" % (time.time() - startTime))
	return primes


sumOfPrimes = sum(getPrimes(1, 100))
print(sumOfPrimes)

