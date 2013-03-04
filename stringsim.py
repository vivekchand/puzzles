# HackerRank/InterviewStreet Problem - String Similarity

def string_sim(substr,string):
	cnt = 0
	for i in xrange(len(substr)):
		if substr[i] == string[i]:
			cnt += 1
		else:
			break
	return cnt

T = int(raw_input())
for i in xrange(T):
	l = []
	text = (raw_input()).strip()
	l.append(text)

	for i in xrange(1,len(text)):
		new = []
		for j in xrange(i,len(text)):
			new.append(text[j])
		adt = ''.join(new)
		if adt in text:
			l.append(''.join(new))	

	sumv = 0
	for i in l:
		val = string_sim(i,text)
		sumv+=val

	print sumv


			
		
