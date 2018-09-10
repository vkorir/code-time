def largest_sum(arr):
	if len(arr) < 2:
		return None

	first, second = 0, 1
	if arr[first] < arr[second]:
		first, second = second, first

	for i in range(2, len(arr)):
		if arr[first] < arr[i]:
			first, second = i, first

	return arr[first] + arr[second]