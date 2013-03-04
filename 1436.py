# SPOJ Problem Set 1436. Is it a tree?
import sys
visited = []
yes = 1
def dfs(u):
	global yes
	global edges
	global visited
	if u not in visited and yes:
		try:
			if edges[edges[u]]:
				v=edges[u]
#				print 'visiting ',v
				visited.append(u)
				dfs(v)
		except:
				return
	else:
		yes = 0

# check if its a tree topology => acyclic graph ?
edges = {}
mn = (raw_input()).split()
n = int(mn[0]) # no. of nodes
m = int(mn[1]) # no. of edges
if 0<n<=10000 and 0<=m<=20000:
	for i in xrange(m):
		uv = (raw_input()).split()
		u = int(uv[0])
		v = int(uv[1])
		if u>=1 and v<=n:
			edges[u] = v

#print edges
#print 'visiting ',1
dfs(1)
if yes:
	print 'YES'
else:
	print 'NO'
