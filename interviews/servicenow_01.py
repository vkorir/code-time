def preorder(root):
	if root is None:	return

	print(root.value)
	preorder(root.left)
	preorder(root.right)

def preorder(root):
	queue = []
	if root is not None:
		queue.append(root)
	while len(queue) > 0:
		node = queue.pop(0)
		print(node.value)
		if node.right is not None:
			queue.append(root.right)
		if node.left is not None:
			queue.append(root.left)
		