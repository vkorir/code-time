def selection_sort(lst):
	res = []

	while len(lst) > 0:
		least = min(lst)
		lst.remove(least)
		res.append(least)

	return res