def convert(s, rows):
    res = [[] for _ in range(rows)]
    index, inc = 0, 1
    for l in s:
        res[index].append(l)
        index = (index + inc) % rows
        if index == rows - 1 and inc > 0:
            inc = -1
        elif index == 0 and inc < 0:
            inc = 1
    # print(res)
    return ''.join(map(lambda s: ''.join(s), res))


print(convert('PAYPALISHIRING', 3))