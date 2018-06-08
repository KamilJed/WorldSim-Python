from WorldSim.Organisms.Animals.Animal import Animal


class Sheep(Animal):

    def __init__(self, x, y, world, strength=None):
        super().__init__(x, y, world, strength)
        self._initiative = 4
        if strength is None:
            self._strength = 4
        self._color = "blue"

    def clone(self, x, y):
        return Sheep(x, y, self._world)

    def getName(self):
        return "Sheep"




