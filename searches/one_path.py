import collections
from auxiliaries.search import generate_neighbors

"""_summary_
Generate one possible path from my starting point to my ending point
"""

def depth_first_search_one(obstacles_edges, obstacles_vertexes, initial_point=(0, 0), target_point=(100, 100)):
    stack = collections.deque([(initial_point, [initial_point])])
    visited = set()
    paths = []

    while stack:
        current, path = stack.pop()

        # Verifica se o nó já foi visitado
        if current in visited:
            continue

        # Adiciona o nó atual à lista de visitados
        visited.add(current)

        if current == target_point:
            paths.append(path)
            continue

        for neighbor in generate_neighbors(obstacles_edges, obstacles_vertexes, current):
            if neighbor not in visited:  # Evita visitar o mesmo nó mais de uma vez
                stack.append((neighbor, path + [neighbor]))

    return paths