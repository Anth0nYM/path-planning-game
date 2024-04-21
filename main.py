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

    criador = ObstacleMaker()
    obs_edges, obs_vertexes = criador.create(34) #seed=2

# Generating paths
    random_paths = generate_random_paths(1, seed=2)
    #dfs_all = all(obs_edges, obs_vertexes)
    dfs_one = one(obs_edges, obs_vertexes)
# Displaying the platform

    plataforma = Platform(obs_edges)
    plataforma.display(dfs_one)

# Depure
    print(dfs_one)
    # print(f"{obs_edges}, \n {obs_vertexes}")
    # vizinhos = generate_neighbors(obs_edges, obs_vertexes)
    # print(vizinhos)
    # for vz in vizinhos:
    #     path.append([(0, 0), vz])
    # plataforma.display(path)
