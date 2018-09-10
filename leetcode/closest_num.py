"""
[1, 2, 3, 4, 5, 6], 25 => 4, 5, 6
[1 2 3] => 19
[2 3 4] => 16 = 19 + 1 - 4
[3 4 5] => 13
[4 5 6] => 10
"""

def closest_sum(arr, n):
	if len(arr) <= 3:
		return arr

	indices = {0, 1, 2}
	curr_sum = n - sum(arr[:3])

	for i in range(3, len(arr)):
		mn, ind = curr_sum, None
		for x in list(indices):
			if abs(curr_sum + arr[x] - arr[i]) < abs(mn):
				mn = curr_sum + arr[x] - arr[i]
				ind = x

		if ind is not None:
			indices.remove(ind)
			indices.add(i)
			curr_sum = mn
	
	return [arr[i] for i in indices]

print(closest_sum([4, 7, -23, 4, 6, 2, 5, 7, 77, 0, 0], -23))