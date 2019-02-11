import unittest


def shuffle(array):
	median = find_median(array)
	
	next_even, next_odd = 0, 1
	res = [0 for _ in array]
	for n in array:
		if n >= median and next_odd < len(array) or next_even >= len(array):
			res[next_odd] = n
			next_odd += 2
		else:
			res[next_even] = n
			next_even += 2
	return res

def find_median(array):
	left, right = [], []
	if len(array) == 1:
		return array[0]
	pivot = array[0]
	for i in range(1, len(array)):
		if array[i] >= pivot:
			right.append(array[i])
		else:
			left.append(array[i])
	if len(left) == len(right):
		return pivot
	if len(left) > len(right):
		return find_median(left)
	return find_median(right)


class Test(unittest.TestCase):
	def test1(self):
		array = [-1, -1, 0, 1, 1]
		output = shuffle(array)

		largest_even = smallest_odd = None
		for i in range(0, len(output), 2):
			if not largest_even or output[i] > largest_even:
				largest_even = output[i]
			if i + 1 < len(array) and (not smallest_odd or output[i+1] < smallest_odd):
				smallest_odd = output[i+1]
		self.assertTrue(largest_even <= smallest_odd)

	def test2(self):
		array = [-1, 5, 10, -1, -5, 1]
		output = shuffle(array)

		largest_even = smallest_odd = None
		for i in range(0, len(output), 2):
			if not largest_even or output[i] > largest_even:
				largest_even = output[i]
			if i + 1 < len(array) and (not smallest_odd or output[i+1] < smallest_odd):
				smallest_odd = output[i+1]
		self.assertTrue(largest_even <= smallest_odd)

if __name__ == '__main__':
	unittest.main()