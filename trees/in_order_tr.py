def in_order_traversal(root):
	stack, res = [], []
	while root or len(stack) > 0:
		while root:
			stack.push(root)
			root = root.left
		root = stack.pop()
		res.append(root.val)
		root = root.right
	return res

def post_order_traversal(root):
	stack, res = [], []
	while root or len(stack) > 0:
		while root:
			if root.right:
				stack.append(root.right)
			stack.append(root)
			root = root.left
		root = stack.pop()
		if root.right and stack[-1] == root.right:
			stack.pop()
			stack.append(root)
			root = root.right
		else:
			res.append(root.data)
			root = None
	return res


def pre_order_traversal(root):
	stack, res = [root], []
	while len(stack) > 0:
		node = stack.pop()
		if not node:
			continue
		res.append(node.val)
		stack.append(node.right)
		stack.append(node.left)
	return res
			