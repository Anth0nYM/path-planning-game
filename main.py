from models.obstacle_maker import ObstacleMaker
from models.platform import Platform
from searches.random_path import generate_random_path
from searches.all_paths import depth_first_search

class Main:
    def __init__(self):
        pass


if __name__ == "__main__":

 # Making obstacles
    criador = ObstacleMaker()  # Create an obstacle maker
    obs_random_edges, obs_random_vertexes = criador.create(1)  # Create random obstacles
    obs_teste = [[[(50, 50), (60, 50)], [(60, 50), (60, 60)], [
        (60, 60), (50, 60)], [(50, 60), (50, 50)]]]  # A simple obstacle
    #print(f"{obs_random_edges}\n\n\n{obs_random_vertexes}")
# Generating paths

    paths = depth_first_search((0,0), (100,100), obs_teste)
    print(paths)
    #print(paths)
    #paths = [generate_random_path(10, 100) for _ in range(10)]  # Random paths
    #path_reto = [[(0, 0), (100, 100)]] # Path from start to end, ignoring obstacles.
    #path_simples = [[(0, 0), (50, 50)], [(50, 50), (60, 50)], [
    #    (60, 50), (60, 60)], [(60, 60), (100, 100)]] # Simple path avoiding an obstacle

# Displaying the platform
    plataforma = Platform(obs_teste)  #Create a platform
    plataforma.display([paths]) # Display the platform with the path
