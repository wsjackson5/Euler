#Project Euler Week 2
#William Jackson

from itertools import compress
import time
from math import log
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


def getPrimes(limit):						#Implement Sieve of Eratosthenes, return all primes up to limit, and time it.
	startTime = time.time()
	num = [x for x in range (limit)]			#Create list of all numbers up to limit.
	bools = [True] * limit					#Create a matching list of booleans, initially all marked as prime.
	for i in num:						#Iterate for every number on list of numbers.
		if (i >= 2):					#Start first sieve at 2.
			if bools[i] == True:			#if number is marked as prime,
				j = 2				#find and mark as not prime eveery multiple up to limit
				while ((i * j) < limit):
					bools[i * j] = False
					j += 1

	bools[0] = False				#Cannot mark multiples of 0 and 1 as not prime, mark 0 and 1 manually.
	bools[1] = False
	getPrimes.num = num
	getPrimes.bools = bools
	primes = list(compress(num, bools))		#Use compress to remove every composite number.
	
	print("- %s seconds -" % (time.time() - startTime))
	return primes

def checkNumber(n):
	while n:
		if n % 10 == 2 or n % 10 == 4 or n % 10 == 5 or n % 10 == 6 or n % 10 == 8:
			return True
	n /= 10
	return False

def checkCircs(numbers):
	remove = []
	for i, x in enumerate(numbers):
		if checkNumber(x):
			remove.append(i)
	array.insert(0, 5)
	array.insert(0, 2)
	return remove

def circ(i):				#Return circulars of a number, in a list of integers.
	j = str(i)
	n = (len(j) - 1)
	k = 0
	circs = []
	while k <= n:
		x = j[k:]+j[:k]		#Rotate to left, append, and rotate left again for number of digits in number.
		circs.append(int(x))
		k += 1
	return circs

def circularPrimes(limit):				#Find number of circular primes up to limit. (Takes ~300 seconds for 1,000,000)
	allPrimes = getPrimes(limit)
	Primes = [x for x in allPrimes if x not in checkCircs(allPrimes)]
	print(len(allPrimes))
	print(len(Primes))
	bools = [False] * len(primes)
	startTime = time.time()
	for i in range (0, len(primes)):		#Iterate each prime number.
		j = int(primes[i])
		circs = circ(j)				#Find rotations.
		if all(x in primes for x in circs):	#Check to see if all rotations are in list of primes, if so mark True.
			bools[i] = True
	
	circPrimes = list(compress(primes, bools))
	print("- %s seconds -" % (time.time() - startTime))	#Time function because this one takes a long time.
	return circPrimes

#sumOfPrimes = sum(getPrimes(2000000))		#Verify prime number generator is working correctly.
#print(sumOfPrimes)
#print(142913828922)

limitCount = 100000
primes = getPrimes(limitCount)
print("Number of primes under" , limitCount,":" , str(len(primes)) , "\n")

n = 100000			#From prime number theorem. Approximate nth prime. 
				#The difference ratio between the estimate and actual is under 1.2 for n > 50.
limitOrderings = int((n * log(n)) * 1.2)
primes = getPrimes(limitOrderings)
print(str(n) + "th prime number: " + str(primes[(n - 1)]) , "\n")

limitProportions = 1000000
primes = getPrimes(limitProportions)
bools = getPrimes.bools
y = []
for z in range (0, 1000):		#Slice up bools from getPrimes function into ranges, and then count and get a ratio for each.
	slic = bools[(z * 1000) : ((z + 1) * 1000)]
	y.append(sum(slic) / 1000)
x = np.arange(0, 1000000, 1000)
plt.ylabel('Proportion')
plt.xlabel('Range')
plt.plot(x, y)
plt.show(block=False)

limitCircular = 1000000
circularCount = circularPrimes(limitCircular)
print("Number of circular primes under" , limitCircular,":" , str(len(circularCount)) , "\n")
