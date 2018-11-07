def is_cyclic():
	visited = {}
	for node in all_nodes:
		if not visited[node]:
			if (is_cyclic_util(node, visited)):
				return True
	return False

def is_cyclic_util(node, visited={}, parent=None):
	
	visited[node] = True # mark current node as visited

	for n in neighbors(node):
		if not visited[n]:	# if neighbor not in visited, recurse in it
			if (is_cyclic_util(n, visited, node)):
				return True
			elif parent != n: # if an adjacent vertex and not parent of current vertex, then there is a cycle
				return True
	return False
