"""_summary_
Generates random paths. (function for plot testing)
"""
import random


def generate_random_paths(num_paths, seed=None, platform_size=100, max_intermediary_points=10):
    random.seed(seed)
    paths = []
    for _ in range(num_paths):
        path = [(0, 0)]
        num_points = random.randint(1, max_intermediary_points)
        for _ in range(num_points):
            x = random.randint(0, platform_size)
            y = random.randint(0, platform_size)
            path.append((x, y))
        path.append((platform_size, platform_size))
        paths.append(path)
    return paths
