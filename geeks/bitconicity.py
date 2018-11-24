def bitconicity(array):
	"""
	i = 1
	B = [0 1 2 3 4]
	"""
	b = 0
	for i in range(1, len(array)):
		if array[i] > array[i - 1]:
			b += 1
		elif array[i] < array[i - 1]:
			b -= 1
	return b