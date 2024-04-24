from models.obstacle_maker import ObstacleMaker
from models.platform import Platform
from searches.random_path import generate_random_paths
from searches.all_paths import depth_first_search as all
from searches.one_path import depth_first_search_one as one
import time


class Main:
    def __init__(self):
        pass


if __name__ == "__main__":
    
    start_time = time.time()

 # MAKING OBSTACLES
    maker = ObstacleMaker()
    obs_edges, obs_vertexes = maker.create(42,seed=2)

# GENERATING PATHS, CHOSE ONE OF 3 METHODS
    # random_paths = generate_random_paths(1, seed=2)
    dfs_one = one(obs_edges, obs_vertexes)
    
    
    # WARNING: When searching all the paths.
    # Be careful with the number of obstacles.
    # (On my machine, I achieved instant results only with 3 obstacles;
    # adding too many could significantly extend the processing time)
    # dfs_all = all(obs_edges, obs_vertexes)




# DISPLAYING PLATFORM
    plataform = Platform(obs_edges)
    
    #if you're using random_paths:
    #plataform.display(random_paths)
    
    #if you're using dfs_one:
    plataform.display(dfs_one)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"{dfs_one} is the path found")
    print(f"{round(execution_time,2)} seconds of execution")
    
    #if you're using dfs_all:
    # highlight_path = 0  # highlight_path is the index of the path you want to highlight
    # plataform.display(dfs_all, highlight_path)
    # print(f"{len(dfs_all)} paths found")
    # print(f"{dfs_all[highlight_path]} is the highlighted path")
    # end_time = time.time()
    # execution_time = end_time - start_time
    # print(f"{round(execution_time,2)} seconds of execution")
