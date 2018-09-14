class Node(object):
	def __init__(self, value, nextNode):
		self.value = value
		self.nextNode = nextNode

class Stack(object):
	def __init__(self):
		self.head = None

	def push(self, value):
		node = Node(value, self.head)
		self.head = node

	def pop(self):
		if self.head is None:
			return None

		value = self.head.value
		self.head = self.head.nextNode

		return value

	def reverse(self):
		pointer = self.head.nextNode
		self.head.nextNode = None

		while pointer is not None:
			temp = pointer.nextNode
			pointer.nextNode = self.head
			self.head = pointer
			pointer = temp
		
