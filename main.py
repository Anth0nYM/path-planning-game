from models.obstacle_maker import ObstacleMaker
from models.platform import Platform
from searches.random_path import generate_random_paths
from auxiliaries.search import generate_neighbors

class Main:
    def __init__(self):
        pass


if __name__ == "__main__":

 # Making obstacles
 
    criador = ObstacleMaker()  
    obs_edges, obs_vertexes = criador.create(1,seed=2)  
    
# Generating paths

    random_paths = generate_random_paths(1,seed=2)  
# Displaying the platform

    plataforma = Platform(obs_edges)  
    plataforma.display(random_paths) 

# Depure
    print(f"{obs_edges}, \n {obs_vertexes}")
    
    vizinhos = generate_neighbors(obs_edges,obs_vertexes)
    print(vizinhos)
    