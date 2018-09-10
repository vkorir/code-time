from collections import deque


def printShortestPath(n, i_start, j_start, i_end, j_end):
    result = findShortestPath(n, i_start, j_start, i_end, j_end, set())
    if result is not None:
        print(result)
    else:
        print('Impossible')


def findShortestPath(n, i_st, j_st, i_en, j_en, seen, fr=None):
    if not (0 <= i_st < n and 0 <= j_st < n and 0 <= i_en < n and 0 <= j_en < n) or (i_st, j_st) in seen:
        return None

    seen.add((i_st, j_st))
    if i_st == i_en and j_st == j_en:
        return [fr]
    i, j = i_st, j_st

    direction = ['UL', 'UR', 'L', 'R', 'LL', 'LR']
    steps = [(i - 2, j - 1), (i - 2, j + 1), (i, j - 2), (i, j + 2), (i + 2, j - 1), (i + 2, j + 1)]
    results = []
    for ind in range(len(direction)):
        i_st, j_st = steps[ind]
        next_step = findShortestPath(n, i_st, j_st, i_en, j_en, seen, direction[ind])
        if next_step is not None:
            results += next_step
    if fr is not None:
        results = [fr] + results
    return results


printShortestPath(7, 6, 6, 0, 1)