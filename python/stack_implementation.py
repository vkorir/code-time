import unittest
# Implement a stack that supports reversing its elements

class Test(unittest.TestCase):
    def test_init(self):
        stack = Stack()
        self.assertEqual(stack.pop(), None, "An empty stack should return None")
    
    def test_push_pop(self):
        stack = Stack()
        stack.push(0)
        self.assertEqual(stack.pop(), 0, "Expected 0")
        self.assertEqual(stack.pop(), None, "The stack should be empty")

        for i in range(5):
            stack.push(i)
        
        self.assertEqual([stack.pop() for _ in range(5)], [4, 3, 2, 1, 0])
    
    def test_reverse(self):
        stack = Stack()

        for i in range(5):
            stack.push(i)
        
        res = stack.reverse()
        self.assertEqual([res.pop() for _ in range(5)], [0, 1, 2, 3, 4])



class Node(object):
    def __init__(self, val, next_node):
        self.value = val
        self.next = next_node

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, val):
        self.head = Node(val, self.head)
    
    def pop(self):
        if self.head is None:
            return None
        val = self.head.value
        self.head = self.head.next
        
        return val

    def reverse(self):
        result = Stack()
        p = self.head
        while p is not None:
            result.push(p.value)
            p = p.next
        return result


if __name__ == '__main__':
    unittest.main()
