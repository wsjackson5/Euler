# Project Euler - Week 1
# William Jackson

element = 1		# Start with first element as 1.
difference = 1		# First difference.
elementNumber = 1	# First element will be element number 1.
parse = 1000		# Number of elements to parse.

sumT = 0
productT = 1
divisibleFiveT = 0

while (elementNumber <= parse):				# Loop  elements.
	sumT = sumT + element				# Add each element to the sum.
	productT = productT*element			# Multiply each element by the product total.
	x = element % 5					# Element modulo 5
	if (x == 0):
		divisibleFiveT = divisibleFiveT + 1
	element = element + difference			# Add the difference to calculate the next element.
	difference = difference + 2			# Add 2 to calculate the next difference.
	elementNumber = elementNumber + 1		# Increment element counter.


print "Sum of first " , parse , " terms: " , sumT
print "Number of first " , parse , " terms evenly divisible by 5: " , divisibleFiveT

tailsRemoved = str(productT).rstrip("0")									# Strip trailing zeros.
print "Last eight digits after removing trailing zeros: " , int(tailsRemoved) % 100000000			# Print (up to) last 8 digits.
