"""_summary_
Generate all possible paths from my starting point to my ending point
"""
from auxiliaries.search import get_neighbors, is_intersecting, move_to_edge
import collections
def dfs(start_point, end_point,obstacles):
    paths = []
    stack = collections.deque(start_point)
    visited = set(start_point)
    node = stack.pop()
    while node != end_point:
        neighbors = get_neighbors(node, obstacles)
        if neighbors == []:
            if not is_intersecting([node,end_point],obstacles):  # Tentando mover diretamente para o ponto final
                return paths
            node = move_to_edge(node,obstacles)
            