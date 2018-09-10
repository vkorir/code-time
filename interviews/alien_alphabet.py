"""
[cccba ccdk a ab]
ccaa
cc b
bd 
ak 

return c a b d k
"""
from collections import deque


def get_order(words):
	seen, result = set(), deque()
	for word in words:
		for (i, ch) in enumerate(word):
			if len(result) == i:
				result.append(deque(ch))
			else:
				result[i].append(ch)
	
	# result = [[ca], [b], []]
	order = deque()
	for chs in result:
		for ch in chs:
			if not ch in seen:
				seen.add(ch)
				order.append(ch)
	return ' '.join(order)


alpha = ['cccba', 'ccdk', 'a', 'ab']
print(get_order(alpha))