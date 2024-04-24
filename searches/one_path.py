import collections
from auxiliaries.search import generate_neighbors


def depth_first_search_one(obstacles_edges, obstacles_vertexes, initial_point=(0, 0), target_point=(100, 100)):
    """_summary_
    Uses DFS (Depth First Search) to generate a possible path from my start point to my end point
    """
    stack = collections.deque([(initial_point, [initial_point])])
    visited = set()
    paths = []

    while stack:
        current, path = stack.pop()

        if current in visited:
            continue

        visited.add(current)

        if current == target_point:
            paths.append(path)
            continue

        for neighbor in generate_neighbors(obstacles_edges, obstacles_vertexes, current):
            if neighbor not in visited:  # Avoid visiting the same node more than once
                stack.append((neighbor, path + [neighbor]))

    return paths
