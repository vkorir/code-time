from math import floor

def divide(x, y):
	if x == 0:	return (0, 0)
	
	(q, r) = divide(floor(x / 2), y)

	q, r = 2 * q, 2 * r
	if x % 2 == 1:	r += 1
	if r >= y:		r, q = r - y, q + 1

	return (q, r)