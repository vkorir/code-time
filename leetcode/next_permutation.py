from functools import reduce


def next_permutation(nums):
    fn = lambda a, b: a*10 + b
    num = reduce(fn, nums)

    nums.sort()

    nextp = reduce(fn, nums)
    loop = False

    while not loop or nextp <= num:
        loop = True
        next_perm(nums)
        nextp = reduce(fn, nums)

    return nextp


def next_perm(perm):
    if len(perm) > 1:
        hi = len(perm) - 1
        lo = hi - 1

        while lo >= 0 and perm[lo] >= perm[hi]:
            lo -= 1
            hi -= 1

        if hi == 0:
            perm[0], perm[len(perm) - 1] = perm[len(perm) - 1], perm[0]
        else:
            perm[lo], perm[hi] = perm[hi], perm[lo]
            sort_right(perm, hi)


def sort_right(perm, start):
    for i in range(start, len(perm)):
        lo = hi = i
        for j in range(i + 1, len(perm)):
            if perm[j] < perm[lo]:
                lo, hi = j, lo
        perm[lo], perm[hi] = perm[hi], perm[lo]


print(next_permutation([3, 2, 1]))