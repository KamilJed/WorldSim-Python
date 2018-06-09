from WorldSim.Organisms.Plants.Plant import Plant


class Dandelion(Plant):

    __pollinationChance = 3

    def __init__(self, x, y, world, strength=None):
        super().__init__(x, y, world, strength)
        self._initiative = 0
        if strength is None:
            self._strength = 0
        self._color = "yellow"

    def clone(self, x, y):
        return Dandelion(x, y, self._world)

    def getName(self):
        return "Dandelion"

    def action(self):
        for i in range(0, Dandelion.__pollinationChance):
            super().action()