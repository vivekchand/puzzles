# SPOJ Problem Set: 2. Prime Generator
# prime no.
# t no of testcases t<=10
# m n 1 <= m <= n <= 1000000000, n-m<=100000

# print m <= p <= n, one no. per line
# testcases seperated by '\n'

# a prime no. is divsible by itself & 1, else it's non prime
# 2,3,5,7 ... are prime no.s

t = int(input())
if t<=10:
	for l in range(t):
		no = map(int,(raw_input()).split())
		m,n = no[0],no[1]
		print '\n'
		i = 0
		j = 0
		if m>=1 and m<=n and n<=1000000000 and n-m<=100000:
			for i in range(m,n+1):  # 1,2,3,4,5,6,7,8,9,10
				for j in range(2,i+1): # 2,2
					if i%j==0 and i!=j:
						break
					if i==j:
						print i
	
