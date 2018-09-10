"""
(1 2 3) (1 3 2) (2 1 3) (2 3 1) (3 1 2) (3 2 1)
"""


def permute(lst):
    if len(lst) == 2:
        yield lst
        yield list(reversed(lst))

    else:
        for i in range(len(lst)):
            for perm in permute(lst[:i] + lst[i + 1:]):
                yield [lst[i]] + perm


def permutations(lst, res=[]):
    """
    [J O N] => [[J O N] [J N O] [O J N] [O N J] [N J O] [N O J]]
    """

    if len(lst) == 2:
        res.append(lst)
        res.append(lst[::-1])
        return

    for i in range(len(lst)):
        left, rest = lst[i], lst[:i] + lst[i+1:]
        print(permutations(rest, res + [left]))

    return res


print(list(permutations(['J', 'O', 'N'])) )
