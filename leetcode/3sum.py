import unittest

class Test(unittest.TestCase):
	def test(self):
		sol = Solution()
		nums = [-1, 2, 1, -4]
		target = 1

		actual = sol.three_sum_closest(nums, target)
		expected = 2

		self.assertEqual(actual, expected)

class Solution(object):
	def three_sum_closest(self, nums, target):
		nums.sort()
		curr = nums[0] + nums[1] + nums[2]

		for i in range(len(nums)):
			if i > 0 and nums[i] == nums[i - 1]:
				continue
			l, r = i + 1, len(nums) - 1

			while l < r:
				val = nums[i] + nums[l] + nums[r]
				if abs(target - val) < abs(target - curr):
					curr = val
				if curr == target:
					return target
				if val < target:
					l += 1
				else:
					r -= 1
		return curr


if __name__ == '__main__':
	unittest.main()