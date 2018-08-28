def a_star(start, goal):

	open_set, closed_set, meta, g_score, f_score = set([start]), set(), dict(), dict(), dict()

	# g_score, h_score vals defaulted to infinity
	g_score[start] = 0.0
	f_score[start] = heuristic(start, goal)

	while len(open_set) > 0:
		curr = open_set.pop() # priority queue

		if curr == goal:
			return contruct_path(meta, curr)

		for n in curr.get_adjacent():
			if neighbor in closed_set:
				continue

			score = g_score[curr] + dist(curr, neighbor)

			if neighbor not in open_set:
				open_set.add(neighbor)

			else if score >= g_score[neighbor]:
				continue

			meta[neighbor] = curr
			g_score[neighbor] = score
			f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)

		open_set.remove(curr)
		closed_set.add(curr)

	return []


def contruct_path(meta, curr):
	path = [curr]

	while curr in meta.keys():
		curr = meta[curr]
		path.append(curr)

	path.reverse()
	return path

