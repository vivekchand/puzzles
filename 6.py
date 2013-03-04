# SPOJ Problem 6. Simple Arithmetics
import sys
def add(a,b):
	c = a+b
	A = [' ',str(a)]
	B = ['+',str(b)]
	C = [' ',str(c)]
	for i in range(len(B)-len(A)):
		A.insert(0,' ')
	A= ''.join(A)
	B= ''.join(B)
	C= ''.join(C)
	print A
	print B
	for i in range(len(B)):
	 sys.stdout.write('-')
	sys.stdout.write('\n')
	print C

def sub(a,b):
	c = a-b
	A = [' ',str(a)]
	B = ['+',str(b)]
	C = [' ',str(c)]

	for i in range(len(B)-len(A)):
		A.insert(0,' ')

	A= ''.join(A)
	B= ''.join(B)
	C= ''.join(C)
	
	print A
	print B
	for i in range(len(B)):
		sys.stdout.write('-')
	sys.stdout.write('\n')
	print C

def mul(a,b):
	c = a*b
	C =	str(c)
	A = [' ',str(a)]
	B = ['*',str(b)]
	for i in range(len(C)-len(A)+1):
		A.insert(0,' ')
	for i in range(len(C)-len(B)):
		B.insert(0,' ')

	Ap = ''.join(A)
	Bp = ''.join(B)
	print Ap
	print Bp
	Bd = str(b)
	n = len(Bd)

	
	for i in range(len(B)-len(Bd)):
	 sys.stdout.write(' ')

	for i in range(len(Bd)):
	 sys.stdout.write('-')
	sys.stdout.write('\n')

	for i in range(len(Bd)):
		p = int(Bd[n-i-1])*a
		P = str(p)
		P = [' ',str(p)]


		if p!=0:
			for i in range(len(C)-len(P)-i):
				P.insert(0,' ')
		else:
			for i in range(len(C)-len(P)+2):
				P.insert(0,' ')

		P= ''.join(P)
		print P

	for i in range(len(A)):
	 sys.stdout.write('-')
	sys.stdout.write('\n')
	print c

add(12345,67890)
sys.stdout.write('\n')
sub(324,111)
sys.stdout.write('\n')
mul(325,4405)

