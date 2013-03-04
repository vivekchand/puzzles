# HackerEarth: Teaching how to draw
import math
N = int(raw_input()) # no of testcases
for i in range(N):
	S = int(raw_input()) # squares available
	q = math.sqrt(S)
	n = int(math.floor(q))
	sum = 0
	for i in range(n):
		sum += (S/(i+1)) - i
		
	print sum
