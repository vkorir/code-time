import sys

class TreeNode:
	def __init__(self, v, l=None, r=None):
		self.val = v
		self.left = l
		self.right = r
		


def valid_bst(root, max_val=sys.maxsize, min_val=-sys.maxsize):
	if root is None:
		return True
	if root.val <= min_val or root.val >= max_val:
		return False
	return valid_bst(root.left, max_val, root.val) and valid_bst(root.right, root.val, min_val)

t = TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(5, TreeNode(4), TreeNode(6)))
print(valid_bst(t))