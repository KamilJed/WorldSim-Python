from WorldSim.Organisms.Plants.Plant import Plant


class Grass(Plant):

    def __init__(self, x, y, world, strength=None):
        super().__init__(x, y, world, strength)
        self._initiative = 0
        if strength is None:
            self._strength = 0
        self._color = "green"

    def clone(self, x, y):
        return Grass(x, y, self._world)

    def getName(self):
        return "Grass"

