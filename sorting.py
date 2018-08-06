import random

def merge_sort(lst):
	return top_down_split_merge(lst, 0, len(lst))

def top_down_split_merge(lst, i, j):
	if j - i <= 1:
		return

	mid = (i + j) // 2

	top_down_split_merge(lst, i, mid)
	top_down_split_merge(lst, mid, j)

	return top_down_merge(lst, i, mid, j)

def top_down_merge(lst, i, mid, j):
	merged = []
	for k in range(i, j):
		if i < mid and (mid >= j or lst[i] <= lst[mid]):
			merged.append(lst[i])
			i += 1
		else:
			merged.append(lst[mid])
			mid += 1
	return merged


def quick_sort(lst):
	if len(lst) <= 1:
		return lst

	pivot = random.choice(lst)
	left = [n for n in lst if n < pivot]
	right = [n for n in lst if n >= pivot]
