"""_summary_
    Obstacle helper functions
"""

def is_colliding(new_obstacle, obstacles,obstacle_size=10):
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

def decompose_obstacle(obstacle,obstacle_size=10):
    """_summary_
    Receives a tuple that corresponds to the bottom left point of an obstacle and returns its edges
    """
    x, y = obstacle
    segments = [
        [(x, y), (x + obstacle_size, y)],
        [
            (x + obstacle_size, y),
            (x + obstacle_size, y + obstacle_size),
        ],
        [
            (x + obstacle_size, y + obstacle_size),
            (x, y + obstacle_size),
        ],
        [(x, y + obstacle_size), (x, y)],
    ]
    return segments