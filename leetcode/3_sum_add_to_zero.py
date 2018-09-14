import unittest

class Test(unittest.TestCase):
	def test(self):
		lst = [-1, 0, 1, 2, -1, -4]

		print(three_sum(lst))

		self.assertTrue(True)

def three_sum(lst):
	res = []

	lst.sort()

	if len(lst) < 3:
		return res

	for i in range(len(lst)):
		if i > 0 and lst[i] == lst[i - 1]:
			continue
		l, r = i + 1, len(lst) - 1

		while l < r:

			val = lst[i] + lst[l] + lst[r]

			if val == 0:
				res.append([lst[i], lst[l], lst[r]])
				l += 1
				r -= 1

			elif val < 0:
				l += 1

			else:
				r -= 1
	return res

if __name__ == '__main__':
	unittest.main()



