"""_summary_
Search helper functions
"""


def generate_neighbors(obstacles_edges, obstacles_vertexes, current_point, target_point=(100, 100)):
    """__summary__
    Generate neighbors of a determinate point."""
    neighbors = []

    for obstacle_vertex in obstacles_vertexes:
        for possible_neighbor in obstacle_vertex:
            possible_neighbor=clean_neighborhood(current_point, possible_neighbor)
            if possible_neighbor is not None and not is_intersecting([current_point, possible_neighbor], obstacles_edges):
                neighbors.append(possible_neighbor)

    if not is_intersecting([current_point, target_point], obstacles_edges):
        neighbors.append(target_point)

    return neighbors


def is_intersecting(segment, obstacles_edges):
    """__summary__
    Check if the segment intersects any obstacle edge."""
    for obstacle in obstacles_edges:
        for edge in obstacle['edges']:
            if do_segments_intersect(segment, edge):
                return True
    return False


def do_segments_intersect(segment1, segment2):
    """__summary__
    Check whether the movement is valid by calculating the determinant."""
    k = segment1[0]
    l = segment1[1]
    m = segment2[0]
    n = segment2[1]
    det = (n[0] - m[0]) * (l[1] - k[1]) - (n[1] - m[1]) * (l[0] - k[0])
    if det == 0:
        return False
    s = ((n[0] - m[0]) * (m[1] - k[1]) - (n[1] - m[1]) * (m[0] - k[0])) / det
    t = ((l[0] - k[0]) * (m[1] - k[1]) - (l[1] - k[1]) * (m[0] - k[0])) / det
    return 0 < s < 1 and 0 < t < 1


def clean_neighborhood(current_point, possible_neighbor):
    if current_point == possible_neighbor:
        return None
    else:
        if (possible_neighbor[0] == current_point[0] + 10 and possible_neighbor[1] == current_point[1] + 10) or \
            (possible_neighbor[0] == current_point[0] + 10 and possible_neighbor[1] == current_point[1] - 10) or \
            (possible_neighbor[0] == current_point[0] - 10 and possible_neighbor[1] == current_point[1] + 10) or \
            (possible_neighbor[0] == current_point[0] - 10 and possible_neighbor[1] == current_point[1] - 10):
            return None
        else:
            return possible_neighbor

