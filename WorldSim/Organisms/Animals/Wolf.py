from WorldSim.Organisms.Animals.Animal import Animal


class Wolf(Animal):

    def __init__(self, x, y, world, strength=None):
        super().__init__(x, y, world, strength)
        self._initiative = 5
        if strength is None:
            self._strength = 9
        self._color = "black"

    def clone(self, x, y):
        return Wolf(x, y, self._world)

    def getName(self):
        return "Wolf"