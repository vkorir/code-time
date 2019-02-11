import random

def encrypt(msg):
	cipher = ''
	key = random.randint(2**10, 2**12)
	bit = 1
	for i in range(len(msg)):
		cipher += chr(ord(msg[i]) | key & bit)
		bit <<= 1
		if bit > key:
			bit = 1
	return [cipher, key]