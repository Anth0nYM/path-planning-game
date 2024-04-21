
import random
from auxiliaries.obstacle import *


class ObstacleMaker:
    """_summary_
    Obstacle generating class
    """

    def __init__(self, obstacle_size=10):
        self.obstacle_size = obstacle_size

    def create(self, num_obstacles, seed=None, platform_size=100):
        """_summary_
        Create a random number of obstacles, represent by a list of tuples, containing the four edges of the obstacle
        """
        random.seed(seed)  # Seed for reproducibility
        new_obstacles = []
        obstacles_generated = 0
        loop_limite = 1000
        while obstacles_generated < num_obstacles:
            obstacle_coords = (
                random.randint(0, platform_size - self.obstacle_size),
                random.randint(0, platform_size - self.obstacle_size),
            )
            if not is_colliding(obstacle_coords, new_obstacles):
                new_obstacles.append(obstacle_coords)
                obstacles_generated += 1
            else:
                loop_limite -= 1
                if loop_limite == 0:
                    print("Unable to generate all obstacles.")
                    print(f"The maximun number of obstacles, each measuring {self.obstacle_size}x{
                          self.obstacle_size} for a plane of size {platform_size}x{platform_size} (in this seed) is {len(new_obstacles)}")
                    print(f"The {len(new_obstacles)} obstacles generated are:")
                    break
        return generate_edges(new_obstacles), generate_vertexes(new_obstacles)
