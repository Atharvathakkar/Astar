def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node

    while open_set:
        n = min(open_set, key=lambda node: g[node] + heuristic(node))
        if n == stop_node:
            break
        open_set.remove(n)
        closed_set.add(n)

        for m, weight in get_neighbours(n):
            if m in closed_set:
                continue
            if m not in open_set or g[n] + weight < g[m]:
                g[m] = g[n] + weight
                parents[m] = n
                open_set.add(m)

    if n != stop_node:
        print('Path does not exist')
        return None

    path = []
    while n != start_node:
        path.append(n)
        n = parents[n]
    path.append(start_node)
    path.reverse()
    print('Path found:', path)


def get_neighbours(n):
    if n in graph_nodes:
        return graph_nodes[n]
    else:
        return []

def heuristic(n):
    heuristics = {
        'India': 11,
        'Afgan': 4,
        'USA': 3,
        'Brazil': 7,
        'Australia': 3,
        'Belgium': 0
    }

    return heuristics[n]


graph_nodes = {
    'India': [('Afgan', 2), ('Australia', 3)],
    'Afgan': [('USA', 1), ('Belgium', 9)],
    'USA': [('Afgan', 1)],
    'Australia': [('Brazil', 6)],
    'Brazil': [('Belgium', 1)]
}

aStarAlgo('India', 'Belgium')

