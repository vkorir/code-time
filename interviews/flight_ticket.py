import sys
from collections import deque


keys = {
    'am': 'Amsterdam',
    'ln': 'London',
    'nb': 'Nairobi',
    'ny': 'New York',
    'sf': 'San Francisco',
    'sg': 'Shanghai',
    'sj': 'San Jose'
}

fares = [
    ['sf', 'ln', 1300],
    ['sf', 'ny', 300],
    ['sf', 'ch', 300],
    ['sf', 'am', 600],
    ['ln', 'sh', 600],
    ['ln', 'nb', 800],
    ['sh', 'nb', 700],
    ['ny', 'am', 500],
    ['am', 'nb', 600],
    ['ch', 'ny', 150],
    ['ny', 'nb', 1000]
]

"""
sf -> nb
    - cost
    - route
    - visited cities

    algo:
    - check if visited && if route < k
    - visit start
    - visit all neighbors
    
"""


def find_up_to_k_bfs(names, data, start, end, k):
    lowest = sys.maxsize
    seen = set()
    best_route = None
    routes = deque()
    fare = deque()
    visiting = deque()

    visiting.append(start)
    fare.append(0)
    st = deque()
    st.append(start)
    routes.append(st)
    
    while len(visiting) > 0:
        city = visiting.popleft()
        cost = fare.popleft()
        route = routes.popleft()

        if city in seen:
            continue

        seen.add(city)
        if city == end:
            if cost < lowest:
                best_route = route
                lowest = cost
            for ct in route:
                if ct in seen:
                    seen.remove(ct)

        elif len(route) < k:
            # visit all neighbors
            for (dp, ds, cs) in data:
                next_route = route.copy()
                if dp == city:
                    visiting.append(ds)
                    fare.append(cost + cs)
                    next_route.append(ds)
                    routes.append(next_route)

    ticket = ' -> '.join([names[k] for k in best_route])
    return ticket + '\ncost: ' + str(lowest)


def find_up_to_k_dfs(names, data, start, end, k):
    route, price = dfs(data, start, end, k, 0)
    return ' -> '.join([names[key] for key in route]) + '\nCost: ' + str(price)


def dfs(data, current, end, k, fare, stops=0):
    if current == end:
        return deque([end]), fare

    if stops == k:
        return None, 0

    best_route = deque()
    price = sys.maxsize
    for (dp, ds, cs) in data:
        if dp == current:
            route, cost = dfs(data, ds, end, k, fare + cs, stops + 1)
            if route is not None and cost < price:
                route.extendleft([current])
                best_route, price = route, cost

    return best_route, price


def ticket(curr, end, k):
    best_route, best_cost = find_route(curr, end, k)
    return ' -> '.join(best_route) + ' Cost: $' + str(best_cost)

def find_route(curr, end, k, cost=0, stops=0):
    if curr == end:
        return [end], cost
    if stops == k:
        return [], sys.maxsize

    best_route, best_cost = [], sys.maxsize

    for (dep, des, cst) in fares:
        if dep == curr:
            route, price = find_route(des, end, k, cost + cst, stops + 1)
            if price < best_cost:
                best_route, best_cost = [curr] + route, price

    return best_route, best_cost


print(ticket('sf', 'nb', 5))
