def moneyChanging(denoms, amount, index=0):
	if amount < 0:
		return False
	if amount == 0:
		return True


	change = []
	for i in range(index, len(denoms)):
		while i < len(denoms) and denoms[i] > amount:
			i += 1

		change.append(denoms[i])
		if moneyChanging(denoms, amount - denoms[i], i):
			return change
		change.pop(-1)

	return change

denoms = sorted([1, 5, 10, 25, 50])
print(moneyChanging(denoms, 41))
