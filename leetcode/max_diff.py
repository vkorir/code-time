"""
[1 2 4 5 6] => 6 - 1 = 5

"""


def max_diff(arr):
    if len(arr) < 2:
        raise Exception('arr should have at least 2 elems')

    smaller = bigger = 0

    for i in range(1, len(arr)):
        if arr[i] < arr[smaller]:
            smaller = i
        if arr[i] > arr[bigger]:
            bigger = i

    return arr[bigger] - arr[smaller]
