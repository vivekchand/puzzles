# SPOJ Problem Set: 24. Small factorials
def fact(n):
	res = 1
	for i in range(1,n+1):
		res = res*i

	return res

t = int(raw_input())
for l in range(t):
	n = int(raw_input())	
	print fact(n)

