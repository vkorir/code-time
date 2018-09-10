"""
3 	5
011
101
001 -> 1

[1, 2, 3, 4, 5]
(1 2) (1 3) (1 4) (1 5) (2 3) (2 4) (2 5) (3 4) (3 5) (4 5)
0 

100	011
101	101
"""

def diff_bits(lst):
	for i in range(len(lst)):
		for j in range(i + 1, len(lst)):
			print(get_diff(lst[i], lst[j]))

def get_diff(i, j):
	count = 0
	i, j = abs(i), abs(j)
	while i > 0 or j > 0:
		if i & 1 == j & 1:
			count += 1
		i >>= 1
		j >>= 1
	return count

diff_bits([1, 2, 3, 4, 5])
