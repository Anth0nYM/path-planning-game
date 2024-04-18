from models.obstacle_maker import ObstacleMaker
from models.platform import Platform
from searches.random_path import generate_random_paths

class Main:
    def __init__(self):
        pass


if __name__ == "__main__":

 # Making obstacles
    criador = ObstacleMaker()  
    obs_random= criador.create(5,42)  
    
# Generating paths

    random_paths = generate_random_paths(10)
    path = [(0, 0),(70,90),(100,100)] # The path variable contains the coordinates that were accessed until reaching the end point
    paths = [path]
# Displaying the platform
    plataforma = Platform(obs_random)  
    plataforma.display(random_paths) 
