import math
from heapq import heappush, heappop


def roundPricesToMatchTarget(prices, target):

    min_diff, rval = None, []
    heap = [(0, 0, 0, [])]	# (index, diff, total, rounded)

    while len(heap) > 0:
        i, diff, total, ret = heappop(heap)

        if i == len(prices):
            if total == target and (not min_diff or diff < min_diff):
                min_diff, rval = diff, ret
                return rval
        else:
            fl, cl = int(math.floor(prices[i])), int(math.ceil(prices[i]))
            heappush(heap, (i + 1, diff + abs(prices[i] - fl), total + fl, ret + [fl]))
            heappush(heap, (i + 1, diff + abs(prices[i] - cl), total + cl, ret + [cl]))

    return rval


prices = [0.7, 2.8, 4.9, 2.5, 4.3, 5.0]
target = 8
print(roundPricesToMatchTarget(prices, target))