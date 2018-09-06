import unittest

class Test(unittest.TestCase):
	def test(self):
		lst = [1,8,6,2,5,4,8,3,7]
		actual = max_water(lst)
		expected = 49
		self.assertEqual(actual, expected)

def max_water(lst):
	max_area = 0

	i, j = 0, len(lst) - 1

	while i < j:
		max_area = max((j - i) * min(lst[i], lst[j]), max_area)

		if lst[i] < lst[j]:
			i += 1
		else:
			j -= 1

	return max_area


if __name__ == '__main__':
	unittest.main()
