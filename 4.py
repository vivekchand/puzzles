# SPOJ Problem 4. Transform the Expression
import string
# Stack Precedence Function
def F(c):
	if c=='+':
		return 2
	elif c=='-':
		return 4
	elif c=='*':
		return 6
	elif c=='/':
		return 8
	elif c=='^':
		return 10
	elif c=='$':
		return 12
	elif c=='(':
		return 0
	elif c=='#':
		return -1
	else:
		return 15

# Input Precedence Function
def G(c):
  if c=='+':
    return 1
  elif c=='-':
    return 3
  elif c=='*':
    return 5
  elif c=='/':
    return 7
  elif c=='^':
    return 9
  elif c=='$':
    return 11
  elif c=='(':
    return 13
  elif c==')':
    return 0
  else:
    return 14


t = int(raw_input())
for l in range(t):
	infix = (raw_input()).strip()
	s=[]			# stack
	top = -1	# stack is empty
	top = top + 1	
	s.insert(top,'#')	# initialize stack to '#'
	postfix = []
	j=0			# o/p empty, so j=0

	for i in range(len(infix)):
		symbol = infix[i]

		# if stack precedence greater than input precedence
		# remove symbol from stack & place into postfix
		while F(s[top]) > G(symbol):
			postfix.append(s[top])	# pop from the stack & place into postfix
			top = top - 1

		if F(s[top]) != G(symbol):
			top = top + 1
			s.insert(top,symbol) # Push symbol on stack
		else:
			top = top - 1 		# Discard ( from stack

	# Pop remaining symbols & place 
	# them in postfix expression

	while s[top] != '#':
		postfix.append(s[top])
		top = top - 1

	print ''.join(postfix)	
	

