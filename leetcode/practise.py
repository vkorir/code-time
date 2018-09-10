from math import sqrt
from collections import deque
from functools import reduce

def is_prime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False

	for div in range(3, int(sqrt(n)) + 1, 2):
		if n % div == 0:
			return False
	return True

def next_prime():
	prime = 2
	while prime > 0:
		if is_prime(prime):
			yield prime
		prime += 1

def prime_factors(n):
	factors = deque()
	for fc in range(2, n):
		if n % fc == 0 and is_prime(fc):
			factors.append(fc)
	return list(factors)

def nth_fibonacci_iter(n):
	curr, nxt, count = 0, 1, 0
	while count < n:
		curr, nxt = nxt, curr + nxt
		count += 1
	return curr

"""
gcd(20, 12) = gcd(12, 8) = gcd(8, 4) = gcd(4, 4) = 4

"""
def gcd(m, n):
	if m < 0 or n < 0:
		raise ValueError('Oh_My_Dude!')
	if m < n:
		return gcd(n, m)
	if n == 0:
		return m
	return gcd(n, m % n)


def repeating_chars(string):
	bit_vector = 0
	for c in string:
		index = ord(c) - ord('a')
		if is_set(bit_vector, index):
			return False, c
		bit_vector = set_bit(bit_vector, index)

	return True

def is_set(bit_vector, index):
	mask = 1 << index
	return bit_vector & mask > 0

def set_bit(bit_vector, index):
	mask = 1 << index
	bit_vector = bit_vector | mask
	return bit_vector

def missing_number(arr):
	n = len(arr) + 1
	expected = n * (n + 1) // 2
	actual = sum(arr)

	return expected - actual

def sum_finder(arr, n):
	seen = set()
	for num in arr:
		if num in seen and n - num in seen:
			return True
		seen.add(num)
		seen.add(n - num)
	return False


