import matplotlib.pyplot as plt
class Platform:
    """_summary_
    Platform class
    """
    def __init__(
        self,
        obstacles,
        obstacle_size=10,
        size=100,
        start_point=(0, 0),
        end_point=(100, 100),
    ):
        self.obstacles = obstacles
        self.start_point = start_point
        self.end_point = end_point
        self.size = size
        self.obstacle_size = obstacle_size

    def display(self, paths):
        """_summary_
        Shows on the platform all the paths found
        """
        plt.figure(figsize=(8, 8))
        plt.gca().set_aspect('equal', adjustable='box')
        for obstacle in self.obstacles:
            for segment in obstacle:
                x_values, y_values = zip(*segment)
                plt.plot(x_values, y_values, color="red")  # Plot obstacles
        for path in paths:
            for segment in path:
                x_values, y_values = zip(*segment)
                plt.plot(x_values, y_values, color="blue")  # Plot each path
        plt.scatter(*self.start_point, color="blue")
        plt.scatter(*self.end_point, color="green")
        plt.xlim(-5, self.size + 5)
        plt.ylim(-5, self.size + 5)
        plt.show()