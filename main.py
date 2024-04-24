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
    obs_edges, obs_vertexes = maker.create(2, seed=2)

# Generating paths, chose one of 3 methods
    # random_paths = generate_random_paths(1, seed=2)
    # Be careful with the number of obstacles,(On my machine, I achieved instant results only with 3 obstacles; adding too many could significantly extend the processing time)
    dfs_all = all(obs_edges, obs_vertexes)
    # dfs_one = one(obs_edges, obs_vertexes)

# Displaying the platform
    plataforma = Platform(obs_edges)
    highlight_path = 0  # highlight_path is the index of the path you want to highlight
    plataforma.display(dfs_all, highlight_path)
    print(f"{len(dfs_all)} \n {dfs_all[highlight_path]}")
