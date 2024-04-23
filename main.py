from models.obstacle_maker import ObstacleMaker
from models.platform import Platform
from searches.random_path import generate_random_paths
from searches.all_paths import depth_first_search as all
from searches.one_path import depth_first_search_one as one


class Main:
    def __init__(self):
        pass


if __name__ == "__main__":

 # Making obstacles
    maker = ObstacleMaker()
    obs_edges, obs_vertexes = maker.create(1, seed=None)

# Generating paths, chose one of 3 methods
    # random_paths = generate_random_paths(1, seed=2)
    # dfs_all = all(obs_edges, obs_vertexes) # Be careful with the number of obstacles,(On my machine, I achieved instant results only with 3 obstacles; adding too many could significantly extend the processing time)
    dfs_one = one(obs_edges, obs_vertexes)

# Displaying the platform
    plataforma = Platform(obs_edges)
    plataforma.display(dfs_one)
