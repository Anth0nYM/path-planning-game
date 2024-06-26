"""_summary_
    Obstacle helper functions
"""


def is_colliding(new_obstacle, obstacles, obstacle_size=10):
    """_summary_
    Checks whether a new obstacle invades the area of an existing one
    """
    new_min_x = new_obstacle[0]
    new_max_x = new_obstacle[0] + obstacle_size
    new_min_y = new_obstacle[1]
    new_max_y = new_obstacle[1] + obstacle_size
    # new_min and new_max are the coordinates of the new obstacle
    for obstacle in obstacles:
        existing_min_x = obstacle[0]
        existing_max_x = obstacle[0] + obstacle_size
        existing_min_y = obstacle[1]
        existing_max_y = obstacle[1] + obstacle_size
        # existing_min and existing_max are the coordinates of an existing obstacle
        x_overlap = new_min_x <= existing_max_x and new_max_x >= existing_min_x
        y_overlap = new_min_y <= existing_max_y and new_max_y >= existing_min_y

        if x_overlap and y_overlap:
            return True

    return False


def generate_edges(bottom_left_coordinates):
    """Generate the edges of the obstacles."""
    obstacles = []
    for bottom_left in bottom_left_coordinates:
        x, y = bottom_left
        edges = [
            [(x, y), (x + 10, y)],
            [(x + 10, y), (x + 10, y + 10)],
            [(x + 10, y + 10), (x, y + 10)],
            [(x, y + 10), (x, y)],
        ]
        obstacle = {"edges": edges}
        obstacles.append(obstacle)
    return obstacles


def generate_vertexes(bottom_left_coordinates):
    """Generate the vertexes of the obstacles."""
    obstacles = []
    for bottom_left in bottom_left_coordinates:
        x, y = bottom_left
        vertexes = [
            (x, y),
            (x + 10, y),
            (x + 10, y + 10),
            (x, y + 10),
        ]
        obstacles.append(vertexes)
    return obstacles
