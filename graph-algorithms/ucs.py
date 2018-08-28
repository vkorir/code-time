def ucs(start, goal):
	"""
	1. Insert the start node into a priority queue
	2. While queue is not empty
	3. Dequeue the maximum priority element from the queue
	4. If current node is goal state, return contruct path
	5. Insert all the neighbors of the current state with cumulative costs as priorities
	6. If neighbor in closed, continue
	7. If neighbor not in open_set, or neighbor in open_set and its cost < cost[current] + dist(current, neightbor),
		update priority in open_set.
	"""