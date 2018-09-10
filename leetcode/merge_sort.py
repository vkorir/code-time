from collections import deque

def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	left, right = arr[:len(arr) // 2], arr[len(arr) // 2:]

	return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
	result = deque()
	l = r = 0
	
	while l < len(left) and r < len(right):
		if left[l] < right[r]:
			result.append(left[l])
			l += 1
		elif left[l] > right[r]:
			result.append(right[r])
			r += 1
		else:
			result.extend([left[l], right[r]])
			l += 1
			r += 1

	result.extend(left[l:])
	result.extend(right[r:])

	return list(result)
