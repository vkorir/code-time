def num_of_pairs(arr, k):
	"""
	[1 3 46 1 3 9] k = 47
	"""
	count, seen = 0, set()

	"""
	for i in range(len(arr)):
		for j in range(i + 1, len(arr)):
			if arr[i] + arr[j] == k and (arr[i], arr[j]) not in seen and (arr[j], arr[i]) not in seen:
				count += 1
				seen.add((arr[i], arr[j]))
				seen.add((arr[j], arr[i]))
	"""

	pairs = {}

	for n in arr:
		if n in pairs and (n, k - n) not in seen and (k - n, n) not in seen:
			count += 1
			seen.add((n, pairs[n]))
			seen.add((pairs[n], n))
		else:
			pairs[n] = k - n
			pairs[k - n] = n

	return count

print(num_of_pairs([6, 6, 3, 9, 3, 5, 1], 12))