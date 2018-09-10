class BST(object):
	def __init__(self, val):
		self.val = val
		self.left = self.right = None

	def add_left(self, val):
		self.left = BST(val)

	def add_right(self, val):
		self.right = BST(val)

	def left_child(self):
		return self.left

	def right_child(self):
		return self.right