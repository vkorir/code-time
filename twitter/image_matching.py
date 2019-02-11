import unittest


class Test(unittest.TestCase):
	def test(self):
		grid1 = ['001', '011', '100']
		grid2 = ['001', '011', '101']
		output = solution(grid1, grid2)
		expected = 1
		self.assertEqual(output, expected)


def solution(grid1, grid2):
	# assume grid1 same shape as grid2
	seen = [[False for _ in range(len(grid1))] for _ in range(len(grid1[0]))]
	matching_regions = 0
	for row in range(len(grid1)):
		for col in range(len(grid1[0])):
			if grid1[row][col] == grid2[row][col] == '1' and not seen[row][col]:
				if region_matches(grid1, grid2, row, col, seen):
					matching_regions += 1
	return matching_regions


def region_matches(grid1, grid2, row, col, seen):
	seen[row][col] = True
	if grid1[row][col] != grid2[row][col]:
		return False
	if grid1[row][col] == '0':
		return True

	for i, j in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
		if i < 0 or j < 0 or i > len(grid1) - 1 or j > len(grid1[0]) - 1 or seen[i][j]:
			continue
		if not region_matches(grid1, grid2, i, j, seen):
			explore_all_adjacent(grid1, grid2, seen, [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)])
			return False

	return True


def explore_all_adjacent(grid1, grid2, seen, neighbors):
	for row, col in neighbors:
		if row < 0 or col < 0 or row > len(grid1) - 1 or col > len(grid1[0]) - 1 or seen[row][col]:
			continue
		if grid1[row][col] == '0' or grid2[row][col] == '0':
			continue
		seen[row][col] = True
		adjacent = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
		explore_all_adjacent(grid1, grid2, seen, adjacent)


if __name__ == '__main__':
	unittest.main()