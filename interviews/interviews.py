def merge2( s ):
    indices = [0] * len(s) # [0 0 0 0 0]
    result = []
    
    while len(s) > 0: # k O(nk)
        
        mn = min([s[i][indices[i]] for i in range(len(s))]) # n

        i = 0
        while i < len(s): # n
            if s[i][indices[i]] == mn:
                indices[i] += 1
                result.append(mn)

            if indices[i] == len(s[i]):
                s.pop(i)
                indices.pop(i)
            else:
                i += 1
    
    return result

"""
[-2 8 7 6 5 4 9 -1]

l = -2 8 7
r = -1 9 
"""

def largest_sum_bf(arr):
	if len(arr) == 0: raise ValueError

	result = arr[0]
	for l in range(1, len(arr) + 1):
		i = 0
		while i + l < len(arr):
			s = sum(arr[i: i + l + 1])
			if s > result:	result = s
			i += 1

	return result

def largest_sum_dc(arr):
	if len(arr) == 0:	raise ValueError
	return div_and_con(arr, 0, len(arr) - 1)

def div_and_con(arr, start, end):
	if start >= end:
		return arr[start]

	mid = (start + end) // 2

	left = div_and_con(arr, start, mid)
	right = div_and_con(arr, mid + 1, end)

	return max(left, right, left + right)

print(largest_sum_dc([-1, 8, 8, -1]))