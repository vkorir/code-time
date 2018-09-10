import random

def merge_sort(lst):
	work = lst[:]
	top_down_split_merge(work, 0, len(lst), lst)

def top_down_split_merge(work, i, j, lst):
	if j - i <= 1:
		return

	mid = (i + j) // 2

	top_down_split_merge(work, i, mid, lst)
	top_down_split_merge(work, mid, j, lst)

	top_down_merge(work, i, mid, j, lst)

def top_down_merge(lst, i, mid, j, lst):
	merged = []
	for k in range(i, j):
		if i < mid and (mid >= j || lst[i] <= lst[mid]):
			merged.push(lst[i])
			i += 1
		else:
			merged.push(lst[mid])
			mid += 1
	return merged


def quick_sort(lst):
	if len(lst) <= 1:
		return lst

	pivot = random.choice(lst)
	left = [n for n in lst if n < pivot]
	right = [n for n in lst if n >= pivot]
