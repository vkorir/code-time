import unittest

class Test(unittest.TestCase):
	def test(self):
		s = 'aaa'
		self.assertTrue(valid_palindrome(s))

		s = 'abbaa'
		self.assertTrue(valid_palindrome(s))

		s = 'abzba'
		self.assertTrue(valid_palindrome(s))

		s = 'abbaaa'
		self.assertFalse(valid_palindrome(s))


def valid_palindrome(s):
	for i in range(len(s)):
		if is_palind(s, i):
			return True
	return False

def is_palind(s, removed):
	i, j = 0, len(s) - 1

	while i < j:
		if i == removed:
			i += 1
		elif j == removed:
			j -= 1
		elif s[i] != s[j]:
			return False
		else:
			i += 1
			j -= 1
	return True


if __name__ == '__main__':
	unittest.main()
