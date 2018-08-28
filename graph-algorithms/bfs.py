from queue import Queue

def BFS(root):
	# queue, set, dict
	open_set = Queue()
	closed_set = set()
	meta = dict()

	# initialize
	meta[root] = (None, None)
	open_set.put(root)

	while open_set.length != 0:
		node = open_set.get()
		if is_goal(node):
			return construct_path(node, meta)

		for (child, action) in adjacent(node):
			if child in closed_set:
				continue
			if not child in open_set:
				meta[child] = (node, action)
				open_set.enque(child)

		closed_set.add(node)

def contrusct_path(node, meta):
	path = list()

	while meta[node] != (None, None):
		node, action = meta[node]
		path.append(action)

	path.reverse()
	return path
