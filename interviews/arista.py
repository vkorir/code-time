import unittest

class TestFib(unittest.TestCase):
    def testSanity(self):
        #                 1   2   3   4   5   6   7   8
        n1 = createList([10, 20, 30, 40, 50, 60, 70, 80])
        fib(n1)
        # printList(n1)
        ans = createList([10, 20, 30, 50, 80])
        self.assertTrue(listsEqual(n1, ans))
        
    def testSanity2(self):
        n1 = createList([10, 20, 30, 40, 50, 60, 70, 80, 90])
        fib(n1)
        # printList(n1)
        ans = createList([10, 20, 30, 50, 80])
        self.assertTrue(listsEqual(n1, ans))
        
    def testSanity3(self):
        n1 = createList([])
        fib(n1)
        # printList(n1)
        ans = createList([])
        self.assertTrue(listsEqual(n1, ans))
    
    def testSanity4(self):
        n1 = createList([10])
        fib(n1)
        # printList(n1)
        ans = createList([10])
        self.assertTrue(listsEqual(n1, ans))
        
    def testSanity5(self):
        n1 = createList([10, 20, 30, 40, 50, 60, 70])
        fib(n1)
        # printList(n1)
        ans = createList([10, 20, 30, 50])
        self.assertTrue(listsEqual(n1, ans))

    def testEqual(self):
        #                 1   2   3   4   5   6   7   8
        n1 = createList([10, 20, 30, 40, 50, 60, 70, 80])
        # fib(n1)
        ans = createList([10, 20, 30, 40, 50, 60, 70, 80])
        self.assertTrue(listsEqual(n1, ans))

    def testNotEqual(self):
        #                 1   2   3   4   5   6   7   8
        n1 = createList([10, 20, 30, 40, 50, 60, 70, 80])
        # fib(n1)
        ans = createList([10, 20, 30, 40, 80])
        self.assertFalse(listsEqual(n1, ans))
  # Write some more test cases

class Node:
    def __init__(self, value, next=None):
        self.next = next
        self.value = value
        
# Given an array, create a linked list with the same elements
def createList(arr):
    p = None
    for i in reversed(range(len(arr))):
        p = Node(arr[i], p)
    
    return p

def printList(l1):
    while l1:
        print(l1.value)
        l1 = l1.next
    

# Given two linked lists, return whether they are equal
def listsEqual(l1, l2):
    while l1 and l2:
        if l1.value != l2.value:
            return False
        l1 = l1.next
        l2 = l2.next
    
    return l1 == l2

# Modify the linked list at node in place to contain 
# only the 1st, 2nd, 3rd, 5th, 8th, 13th..., etc. elements.
def fib(node):
    """
    10, 20, 30, 40, 50, 60, 70, 80 -> 10 20 30
                                      1 2  3
    1    1   2  3 .  5 . 8 
    """
    index =  1
    prev = None
    fn = next_fib()
        
    while node:
        if index == fn(index):
            # print("node's value", node.value)
            index += 1
            prev = node
            node = node.next
        else:
            prev.next = node.next
            node = node.next
            index += 1
            

def next_fib():
    prev, curr = 0, 1
    
    def inner_fib(index):
        nonlocal prev, curr
        if index <= curr:
            return curr
        while curr < index:
            prev, curr = curr, prev + curr
        return curr
    
    return inner_fib

if __name__ == "__main__":
    unittest.main()

