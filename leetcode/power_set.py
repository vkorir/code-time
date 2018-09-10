"""
{a b c} = {{} {a} {b} {c} {a b} {a c} {b c} {a b c}}

- all subsets of len 1
- ...
- the subest of len len(arr)

[a b c]
[1 2] [2 3] [1 2 3]

[1 2 3] => [[1] [2] [3] [1 2] [2 3] [1 2 3]]

len + 1 = 4
i = 3
start = 1
start + i = 4
"""

def power_set(arr):
	result = []
	for i in range(1, len(arr) + 1):
		start = 0
		while start + i <= len(arr):
			result.append(arr[start: start + i])
			start += 1
	return result


def subsets(arr):
	subs, res = [], []
	find_subsets(arr, 0, subs, res)
	return res


def find_subsets(arr, index, subset, res):
	for i in range()


print(power_set([1, 2, 3]))