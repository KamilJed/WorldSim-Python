from WorldSim.Organisms.Plants.Plant import Plant


class Guarana(Plant):

    def __init__(self, x, y, world, strength=None):
        super().__init__(x, y, world, strength)
        self._initiative = 0
        if strength is None:
            self._strength = 0
        self._color = "#ccc"
        self._boost = 3

    def clone(self, x, y):
        return Guarana(x, y, self._world)

    def getName(self):
        return "Guarana"