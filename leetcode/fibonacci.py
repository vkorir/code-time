import timeit

def fib1(n):
	if n == 0:	return 0
	if n == 1: 	return 1
	return fib1(n - 1) + fib1(n - 2)

def fib2(n):
	if n == 0:	return 0
	if n == 1: 	return 1

	prev, curr = 0, 1

	for _ in range(n - 1):
		prev, curr = curr, curr + prev

	return curr

def time_fib1():	return fib1(10)
def time_fib2():	return fib2(10)
