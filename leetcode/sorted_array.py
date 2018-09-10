def sorted_array(arr, start=0, end=len(arr)-1):
	if start == end:
		return -1
	mid = (start + end) // 2
	if arr[mid] == mid:
		return mid
	if arr[mid] > mid:
		return sorted_array(arr, start, mid)
	return sorted_array(arr, mid, end)
