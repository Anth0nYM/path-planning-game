"""_summary_
Generates random paths, which do not necessarily go from the starting point to the end (function for plot testing)
"""
import random

def generate_random_path(length, size):
    path = []
    current_point = (0, 0)
    for _ in range(length):
        next_x = random.randint(0, size)
        next_y = random.randint(0, size)
        path.append([current_point, (next_x, next_y)])
        current_point = (next_x, next_y)
    return path
