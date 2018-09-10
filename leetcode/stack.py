## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.

# void push(Object obj)
# Object pop()

# void reverse()

class Node:
    def __init__(self):
        self.value = None
        self.nextNode = None
    

class Stack:
    def __init__(self):
        self.stack = None
        self.size = 0
    
    def pop(self):
        if self.size == 0:
            return None
        value = self.stack.value
        self.stack = self.stack.nextNode
        self.size -= 1
        return value
    
    def push(self, value):
        node = Node()
        node.value = value
        node.nextNode = self.stack
        self.stack = node
        self.size += 1
    
    def reverse(self):
        p = self.stack.nextNode
        for _ in range(self.size):
            self.stack.nextNode = p
            p = p.nextNode
        self.stack = p

