import unittest

class Test(unittest.TestCase):
    """
    [1 2 3] => [[1] [1 2] [1 2 3] [1 3] [2] [2 3] [3]]
    """
    def test(self):
        arr = [1, 2, 3]
        actual = subsets(arr)
        expected = [[1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        self.assertEqual(actual, expected)

def subsets(arr):
    subset, res = [], []
    find_subsets(arr, 0, subset, res)
    return res

def find_subsets(arr, index, subset, res):
    for i in range(index, len(arr)):
        subset.append(arr[i])
        res.append(subset[:])
        find_subsets(arr, i + 1, subset, res)
        subset.pop()

if __name__ == '__main__':
    unittest.main()

