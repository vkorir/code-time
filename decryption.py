from encryption import encrypt

def decryption(cipher, key):
	msg = ''
	bit = 1
	for i in range(len(cipher)):
		msg += chr(ord(cipher[i]) | key & bit)
		bit <<= 1
		if bit > key:
			bit = 1
	return msg

cipher, key = encrypt('hello there.')
print (decryption(cipher, key))
