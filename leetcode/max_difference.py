import sys

def max_difference(arr):
	"""
	[4 1 2 3] => a[3] - a[1] = 2
	first, last
	- if ind[l] == ind[f]: return diff
	- if first >= last, f++
	- if last > first, record diff. repeat
	d = 6

	[2, 3, 10, 2, 4, 8, 1]
	f = 0
	l = 6
	"""
	if len(arr) < 2:	return 0
	max_val = res = -sys.maxsize

	for i in reversed(range(len(arr))):
		if arr[i] > max_val:	max_val = arr[i]
		temp = max_val - arr[i]
		if temp > res:	res = temp

	return res

	

print(max_difference([2, 3, 10, 2, 4, 8, 1]))