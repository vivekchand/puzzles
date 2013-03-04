# SPOJ Problem 5. The Next Palindrome

def is_palindrome(num):
	l = (str(num))
	pal = 1
	for i in range(len(l)):
		if l[i] != l[len(l)-i-1]:
			pal = 0

	return pal

t = int(raw_input())
for x in range(t):
	n = int(raw_input())
	while True:
		n = n + 1
		if is_palindrome(n):
			print n
			break
 

