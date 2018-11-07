def traversal(root):
	levels = {}
	queue = [(root, 0)]

	while len(queue) > 0:
		node, level = queue.pop(0)
		if not node:
			continue
		if level not in levels:
			levels[level] = []
		levels[level].append(node.val)

		queue.append((node.left, level + 1))
		queue.append((node.right, level + 1))

	res = [None for _ in levels.keys()]
	for level, vals in levels.items():
		res[level] = vals
	return res