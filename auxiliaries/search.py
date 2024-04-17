"""_summary_
Search helper functions
"""
def segments_intersect(segment1, segment2):
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

def is_intersecting(segment, segment_list):
    for segment_n in segment_list:
        for seg in segment_n:
            if segments_intersect(segment, seg):
                return True
    return False



def get_neighbors(node, obstacles):
    """Apply the function above in the list of obstacles, to get the neighboors."""
    neighbors = []
    for obstacle in obstacles:
        for edge in obstacle:
            if segments_intersect([node, node], edge):  # Checks whether the segment between the node and the obstacle vertex is valid
                neighbors.append(edge[0])  # Add obstacle vertex as neighbor
    return neighbors

def find_neighbor_in_obstacle(node, obstacles):
    for obstacle in obstacles:
        for edge in obstacle:
            if node in edge:  
                idx = edge.index(node)
                next_vertex_idx = (idx + 1) % 2  # Gets the index of the next vertex on the same edge
                next_vertex = edge[next_vertex_idx]
                return next_vertex
    return None 

obstacles = [[(0, 0), (50, 50)], [(50, 50), (60, 50)], [(60, 50), (60, 60)], [(60, 60), (100, 100)]]


node1 = (50, 50)
neighbor1 = find_neighbor_in_obstacle(node1, obstacles)
print("Ponto 1:", node1)
print("Vizinho 1:", neighbor1)


node2 = (60, 50)
neighbor2 = find_neighbor_in_obstacle(node2, obstacles)
print("Ponto 2:", node2)
print("Vizinho 2:", neighbor2)


node3 = (10, 10)
neighbor3 = find_neighbor_in_obstacle(node3, obstacles)
print("Ponto 3:", node3)
print("Vizinho 3:", neighbor3)