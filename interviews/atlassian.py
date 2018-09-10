import unittest


class Test(unittest.TestCase):
    def testSanity1(self):
        res = maxPoints([1, 2, 1, 3, 2, 3])
        self.assertEqual(res, 8)

    def testSanity2(self):
        res = maxPoints([1,2,3,4,5,6,7,8,9,10,0])
        self.assertEqual(res, 30)


def maxPoints(elements):
    if len(elements) == 0:
        return 0
    max_points = 0

    for elem in elements:
        points, arr = 0, []

        for n in elements:
            if n == elem:
                points += n
            elif n not in (elem - 1, elem + 1):
                arr.append(n)

        points += maxPoints(arr)

        if points > max_points:
            max_points = points

    return max_points


if __name__ == '__main__':
    unittest.main()