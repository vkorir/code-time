def merge_sort(lst):
	if len(lst) <= 1:
		return lst

	mid = len(lst) // 2
	left, right = merge_sort(lst[:mid]), merge_sort(lst[mid:])
	return merge(left, right)

def merge(left, right):
	i = j = 0
	merged = [None] * (len(left) + len(right))

	for k in range(len(left) + len(right)):
		if i < len(left) and (j >= len(right) or left[i] <= right[j]):
			merged[k] = left[i]
			i += 1
		else:
			merged[k] = right[j]
			j += 1

	return merged