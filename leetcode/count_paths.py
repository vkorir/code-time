class Node(object):
    def __init__(self, value):
        self.value = value
        self.neighbors = []


nd = {'a': Node('A'), 'b': Node('B'), 'c': Node('C'), 'd': Node('D'), 'e': Node('E')}
a, b, c, d, e = nd['a'], nd['b'], nd['c'], nd['d'], nd['e']

a.neighbors = ['b', 'c', 'e']
b.neighbors = ['d', 'e']
c.neighbors = ['e']
d.neighbors = ['c']
e.neighbors = []


def count_paths(cur, end):
    """
    - dfs
    - avoid cycles
    """
    res = [0]
    counter(cur, end, res)
    return res[0]


def counter(cur, end, res):
    if cur == end:
        res[0] += 1
        return
    for n in nd[cur].neighbors:
        counter(n, end, res)


print(count_paths('a', 'e'))