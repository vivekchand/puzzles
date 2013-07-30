# SPOJ Problem 6471. Printing some primes

count = 0
first = 1
for i in xrange(2,100000001):
	prime = 1
	for j in xrange(2,i):
		if i%j==0:
			prime = 0
			break
		
	if prime:
		if first:
			print i
			first = 0

		count += 1
		if count == 101:
			print i
			count = 0
	
