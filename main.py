from models.obstacle_maker import ObstacleMaker
class Main:
    def __init__(self):
        pass

if __name__ == "__main__":
    criador = ObstacleMaker()
    obs_teste = criador.create(5,seed=42)
    print(obs_teste)



