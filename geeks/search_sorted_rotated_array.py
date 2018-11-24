def binary_search(array, n):
	pivot = find_pivot(array, 0, len(array) - 1)
	if pivot == -1:
		return search_util(array, 0, len(array) - 1, n)
	if array[pivot] == n:
		return pivot
	if array[0] <= n:
		return search_util(array, 0, pivot - 1, n)
	return search_util(array, pivot + 1, len(array) - 1, n)


def find_pivot(array, lo, hi):
	if hi < lo:
		return -1
	if hi == lo:
		return lo
	mid = (lo + hi) // 2	# lo + (hi - lo) // 2
	if mid < hi and array[mid] > array[mid + 1]:
		return mid
	if mid > lo and array[mid] < array[mid - 1]:
		return mie - 1
	if array[lo] >= array[mid]:
		return find_pivot(array, lo, mid - 1)
	return find_pivot(array, mid + 1, hi)

def search_util(array, lo, hi, n):
	if hi < lo:
		return -1
	mid = (lo + hi) // 2
	if array[mid] == n:
		return mid
	if array[mid] < n:
		return search_util(array, mid + 1, hi, n)
	return search_util(array, lo, mid - 1, n)