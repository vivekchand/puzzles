# SPOJ Problem 7676. Sum of Digits

while True:
	ab = ((raw_input()).strip()).split()
	a= int(ab[0])
	b= int(ab[1])
	if a==-1 and b==-1:
		break
	if a>=0 and b>=0 and a<=1000000000 and b<=1000000000:
		sumval = 0
		for i in range(a,b+1):
			digits = str(i)
			for j in range(len(digits)):
				sumval = sumval + int(digits[j])
	
		print sumval


