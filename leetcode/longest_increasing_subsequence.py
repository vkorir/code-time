def longestIncreasingSubsequence(arr):
    if len(arr) == 0: return
    longestI = [0] * len(arr)
    smallestIndex = 0
    for (i, num) in enumerate(arr):
        if arr[smallestIndex] >= arr[i]:
            longestI[i] = 1
            smallestIndex = i
            continue
        largest, j = smallestIndex, 0
        while j < i:
            if arr[largest] <= arr[j] < arr[i]:
                largest = j
            j += 1
        longestI[i] = 1 + longestI[largest]

    print(arr)
    print(longestI)
    return max(longestI)


seq = [7, 5, 9, 1, 6, 2, 4, 3, 8, 10]
print(longestIncreasingSubsequence(seq))
