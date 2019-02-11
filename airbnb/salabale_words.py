import unittest


class Test(unittest.TestCase):
	def test(self):
		words = ['abb']
		output = solution(words)
		expected = [1]
		self.assertEqual(output, expected)


def solution(words):
	res = []
	for word in words:
		consecutive, replaced = 1, 0
		for i in range(1, len(word)):
			if word[i] == word[i-1]:
				consecutive += 1
			else:
				replaced += count_replaced_util(consecutive)
				consecutive = 1
		replaced += count_replaced_util(consecutive)
		res.append(replaced)
	return res


def count_replaced_util(consecutive):
	if consecutive == 1:
		return 0
	return consecutive // 2 if consecutive % 2 == 0 else consecutive // 3


if __name__ == '__main__':
	unittest.main()