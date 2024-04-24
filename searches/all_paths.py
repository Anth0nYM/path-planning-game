from auxiliaries.search import generate_neighbors
import collections

def depth_first_search(obstacles_edges, obstacles_vertexes, initial_point=(0, 0), target_point=(100, 100)):
    """_summary_
    Generate all possible paths from my starting point to my ending point
    """
    stack = collections.deque([(initial_point, [initial_point])])
    paths = []

    while stack:
        current, path = stack.pop()

        if current == target_point:
            paths.append(path)
            continue

        for neighbor in generate_neighbors(obstacles_edges, obstacles_vertexes, current):
            if neighbor not in path:  # bypass cycles
                stack.append((neighbor, path + [neighbor]))

    return paths


