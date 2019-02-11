def validate_bst(root):
	stack = [(root, -float('inf'), float('inf'))]
	while len(stack) > 0:
		node, mn, mx = stack.pop()
		if not node:
			continue
		if node.val <= mn or node.val >= mx:
			return False
		
		stack.append((node.left, mn, node.val))
		stack.append((node.right, node.val, mx))
	return True