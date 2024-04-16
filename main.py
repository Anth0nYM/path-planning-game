from models.obstacle_maker import ObstacleMaker
from models.platform import Platform


class Main:
    def __init__(self):
        pass


if __name__ == "__main__":
    path_reto = [[(0, 0), (100, 100)]]
    
    path_simples = [[(0, 0), (50, 50)], [(50, 50), (60, 50)], [
        (60, 50), (60, 60)], [(60, 60), (100, 100)]]
    
    criador = ObstacleMaker()
    
    obs_random = criador.create(20, seed=42)
    
    obs_teste = [[[(50, 50), (60, 50)], [(60, 50), (60, 60)], [
        (60, 60), (50, 60)], [(50, 60), (50, 50)]]]
    
    paths = [path_simples, path_reto,]
    plataforma = Platform(obs_random)
    plataforma.display(paths)
