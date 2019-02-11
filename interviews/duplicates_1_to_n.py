def find_duplicates(arr):
	for i in range(len(arr)):
		if arr[abs(arr[i])] < 0:
			return abs(arr[abs(arr[i])])
		arr[abs(arr[i])] = -arr[abs(arr[i])]
	return -1


arr = [1, 2, 2, 3]
print(find_duplicates(arr))