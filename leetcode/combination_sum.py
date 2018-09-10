class Solution:
    def combination_sum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

        dfs graph traversal.

        [2 3 6 7] 7
        2 5: 2 3: 3 0: => [2 2 3]

        """
        res = []
        candidates.sort()
        self.find_path(candidates, target, 0, [], res)
        return res

    def find_path(self, nums, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            if path not in res:
                res.append(path)
            return
        for i in range(index, len(nums)):
            self.find_path(nums, target - nums[i], i + 1, path + [nums[i]], res)


# s = Solution()
# print(s.combination_sum([10, 1, 2, 7, 6, 1, 5], 8))


def combination_sums(arr, num):
    res = []
    path = []
    arr.sort()
    find_sum(arr, num, 0, path, res)
    return res

def find_sum(arr, num, index, path, res):
    if num == 0:
        res.append(path)
        return
    if num < 0:
        return
    for i in range(index, len(arr)):
        find_sum(arr, num - arr[i], i, path + [arr[i]], res)

print(combination_sums([2, 4, 6, 8], 8))