from math import sqrt
import random

def to_binary(n):
	if n == 0:
		return 0
	res = ''
	while n > 0:
		res = str(n & 1) + res
		n >>= 1
	return int(res)
