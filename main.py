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
    obs_random = criador.create(1)  # Create random obstacles
    #obs_teste = [[[(50, 50), (60, 50)], [(60, 50), (60, 60)], [
    #    (60, 60), (50, 60)], [(50, 60), (50, 50)]]]  # A simple obstacle

# Generating paths

    # paths = depth_first_search((0,0), (100,100), obs_random)
    # for path in paths:
        # print(path)
    #paths = [generate_random_path(10, 100) for _ in range(10)]  # Random paths
    #path_reto = [[(0, 0), (100, 100)]] # Path from start to end, ignoring obstacles.
    #path_simples = [[(0, 0), (50, 50)], [(50, 50), (60, 50)], [
    #    (60, 50), (60, 60)], [(60, 60), (100, 100)]] # Simple path avoiding an obstacle

# Displaying the platform
    plataforma = Platform(obs_random)  #Create a platform
    #plataforma.display([paths]) # Display the platform with the path
