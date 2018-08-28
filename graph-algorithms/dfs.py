def DFS(G, v):
	"""
	label v as discovered
	for all edges v to w in G.adjacent(v):
		if w is not labelled discovered:
			recursively call DFS(G, w)
	"""
	return None

def DFS_iterative(G, v):
	"""
	let S be a stack
	S.push(v)
	while S is not empty:
		n = S.pop()
		if n is not labelled as discovered:
			label n as discovered
			for all edges (n, w) in G.adjacent(n):
				S.push(w)
	"""

