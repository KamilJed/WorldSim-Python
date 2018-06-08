from WorldSim.Organisms.Plants.Plant import Plant


class DeadlyNightsahde(Plant):

    def __init__(self, x, y, world, strength=None):
        super().__init__(x, y, world, strength)
        self._initiative = 0
        if strength is None:
            self._strength = 99
        self._color = "cyan"
        self._poisonous = True

    def clone(self, x, y):
        return DeadlyNightsahde(x, y, self._world)

    def getName(self):
        return "DeadlyNightsahde"