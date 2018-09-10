import math

def multiply(x, y):
	if y == 0:	return 0
	z = multiply(x, math.floor(y / 2))

	if y % 2 == 0:
		return 2 * z
	return x + 2 * z

