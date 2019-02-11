class Node(object):
	def __init__(self, val):
		self.val = val
		self.children = {}

class Trie(object):
	def __init__(self):
		self.head = Node('')

	def add_word(self, word):
		node = self.head
		i = 0
		while word[i] in node.children:
			node = node.children[word[i]]
			i += 1
		while i < len(word):
			node.children[word[i]] = Node(word[i])
			node = node.children[word[i]]
			i += 1


def ordering(words):
	trie = Trie()
	for word in words:
		trie.add_word(word)

	res, seen = [], set()
	queue = [trie.head]
	while len(queue) > 0:
		node = queue.pop(0)
		if not node.val or node.val in seen:
			continue
		
		res.append(node.val)
		seen.add(node.val)
		
		queue.extend(list(node.children.values()))
	return res


print(ordering(['aa', 'ab']))
print(ordering(['aa', 'ab', 'cab', 'cac']))