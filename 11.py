# SPOJ Problem 11. Factorial
def fact(n):
	res = 1
	for i in xrange(1,n+1):
		res = res*i
	return res

t = int(raw_input())
for l in range(t):
	no = int(raw_input())
	R = str(fact(no))
	cnt = 0
	n = len(R)-1
	for i in xrange(n):
		if R[n-i] == '0':
			cnt = cnt + 1
		else:
			break
	print cnt
