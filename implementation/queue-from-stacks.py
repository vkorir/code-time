import unittest

class Test(unittest.TestCase):
	def test(self):
		queue = Queue2Stacks()

		self.assertEqual(queue.dequeue(), None, "An empty queue should return None")

		queue.enqueue(0)
		self.assertEqual(queue.dequeue(), 0, "Expected 0")

		queue.enqueue(0)
		queue.enqueue(1)
		self.assertEqual(queue.dequeue(), 0, "Expected 0")
		self.assertEqual(queue.dequeue(), 1, "Expected 1")

		[queue.enqueue(n) for n in range(5)]
		expected = list(range(5))
		actual = [queue.dequeue() for _ in range(5)]
		self.assertEqual(expected, actual, 'Expected ' + str(expected) + ' but got ' + str(actual))

		[queue.enqueue(n) for n in range(3)]
		expected = list(range(2))
		actual = [queue.dequeue() for _ in range(2)]
		self.assertEqual(actual, expected)

		[queue.enqueue(n) for n in range(3, 6)]
		actual = [queue.dequeue() for _ in range(2, 5)]
		expected = list(range(2, 5))
		self.assertEqual(actual, expected)

		actual = queue.dequeue()
		self.assertEqual(actual, 5)


class Queue2Stacks(object):

	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def enqueue(self, element):
		"""
		idea: for enqueue, move all elements from
		stack2 to stack1, then enqueue to stack1
		"""

		# move items from stack2 to stack1
		while len(self.stack2) > 0:
			item = self.stack2.pop()
			self.stack1.append(item)


		# enque to stack1
		self.stack1.append(element)


	def dequeue(self):
		"""
		idea: for deque, move all items from
		stack1 to stack2, then dequeue from
		stack2
		"""

		# move items from stack1 to stack2
		while len(self.stack1) > 0:
			item = self.stack1.pop()
			self.stack2.append(item)

		# dequeue from stack2
		if len(self.stack2) == 0:
			return None
		return self.stack2.pop()


if __name__ == '__main__':
	unittest.main()