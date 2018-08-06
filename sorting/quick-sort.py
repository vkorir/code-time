def quick_sort(lst):
	return quick_sort_in_place(lst, 0, len(lst) - 1)

def quick_sort_in_place(lst, lo, hi):
	if lo < hi:
		pivot = partition(lst, lo, hi)
		quick_sort_in_place(lst, lo, pivot)
		quick_sort_in_place(lst, pivot + 1, hi)

def partition(lst, lo, hi):
	pivot = lst[lo]
	i, j = lo, hi

	while True:
		while lst[i] < pivot:
			i += 1

		while lst[j] > pivot:
			j -= 1

		if i >= j:
			return j

		lst[i], lst[j] = lst[j], lst[i]