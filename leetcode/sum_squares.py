import sys
from math import sqrt

"""
1+1+1+1+...+1 = 12
4+4+4 = 12
9+1+1+1

dfs
12 = 1+1+1+1+..
12 = 1+1+1+1+2
nums = 1...sqrt(n)
"""

def sum_squares(n, index=1, total=0, path=[]):
	if total > n:
		return []
	if total == n:
		return path
	shortest, ln = [], sys.maxsize
	for i in range(index, int(sqrt(n))):
		sums = sum_squares(n, i, total + i**2, path+[i**2])
		if 0 < len(sums) < ln:
			shortest, ln = sums, len(sums)

	return shortest

print(sum_squares(12))