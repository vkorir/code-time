# Complete the function below.
def illuminated(N, pos, lampDBX, lampDBY):
    x, y = pos
    adjacent = ((x,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1),(x-1,y-1),(x-1,y))

    if len(lampDBX[x]) > 0:
        for yPos in lampDBX[x]:
            if (x, yPos) not in adjacent:
                return 'LIGHT'
    if len(lampDBY[y]) > 0:
        for xPos in lampDBY[y]:
            if (xPos, y) not in adjacent:
                return 'LIGHT'
    diff = 1
    while x + diff <= N or x - diff >= 1 or y + diff <= N or y - diff >= 1:
        nw = (x - diff, y + diff)
        ne = (x + diff, y + diff)
        se = (x + diff, y - diff)
        sw = (x - diff, y - diff)

        for coord in [nw, ne, se, sw]:
            cX, cY = coord
            if cX in lampDBX and cY in lampDBX[cX] and (cX, cY) not in adjacent:
                return 'LIGHT'
            if cY in lampDBY and cX in lampDBY[cY] and (cX, cY) not in adjacent:
                return 'LIGHT'
        diff += 1

    return 'DARK'

def checkIllumination(N, lamps, queries):
    lampDBX, lampDBY = {}, {}

    for i in range(1, N + 1):
        lampDBX[i], lampDBY[i] = set(), set()

    for lamp in lamps:
        x, y = lamp
        lampDBX[x].add(y)
        lampDBY[y].add(x)

    return [illuminated(N, pos, lampDBX, lampDBY) for pos in queries]


lambs = [[4,3],[4,4]]
qs = [[3,4],[7,6]]
print(checkIllumination(8, lambs, qs))