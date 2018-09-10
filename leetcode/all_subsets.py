"""
[1 2 3] => [[1] [1 2] [1 2 3] [1 3] [2] [2 3] [3]]
"""


def all_subsets(arr):
    res = []
    for i in range(len(arr)):
        l = 1
        while i + l <= len(arr):
            res.append(arr[i: i + l])
            l += 1
    return res


def subsets(arr):
    subset, res = [], []
    find_subsets(arr, 0, subset, res)
    return res


def find_subsets(arr, index, subset, res):
    for i in range(index, len(arr)):
        subset.append(arr[i])
        res.append(subset[:])
        find_subsets(arr, i + 1, subset, res)
        subset.pop(-1)
    return


print(subsets([1, 2, 3]))

