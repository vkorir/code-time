def rotate_array(array, d):
	"""
	time: O(n)
	space: O(1)
	"""
	n = len(array)
	for i in range(gcd(n, d)):
		temp = array[i]
		j = i
		while True:
			k = (j + d) % n
			if k == i:
				break
			array[j] = array[k]
			j = k
		array[j] = temp
