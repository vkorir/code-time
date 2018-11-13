def binary_search(array, target):
    left, right = 0, 1
    while array[right] < target:
        left, right = right, right * 2
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


array = [-1, 0, 3, 5, 9, 12]
target = 9
print(binary_search(array, 9))
