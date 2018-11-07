def topological_sort(graph):
	stack, visited = [], set()
	for v in range(len(graph)):
		if v not in visited:
			sort_util(graph, v, visited, stack)
	return stack


def sort_util(graph, v, visited, stack):
	visited.add(v)
	neighbors = [i for i in range(len(graph)) if graph[v][i] == '1' and v != i]
	for n in neighbors:
		if n not in visited:
			sort_util(graph, n, visited, stack)
	stack.insert(0, v)


graph = ['100000', '010000', '001100', '010100', '110010', '101001']
print(topological_sort(graph))
