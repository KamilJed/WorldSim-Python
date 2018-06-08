from WorldSim.Organisms.Animals.Escaper import Escaper
from Lib import random


class Antelope(Escaper):

    def __init__(self, x, y, world, strength=None):
        super().__init__(x, y, world, strength)
        self._initiative = 4
        if strength is None:
            self._strength = 4
        self._color = "orange"

    def clone(self, x, y):
        return Antelope(x, y, self._world)

    def getName(self):
        return "Antelope"

    def action(self):
        super().action()
        if self._alive:
            super().action()

    def escape(self, organism, dX, dY):
        import WorldSim.Organisms.Plants.Plant
        if isinstance(organism, WorldSim.Organisms.Plants.Plant.Plant):
            return False
        if random.randrange(0, 100, 1) <= 50:
            return super().escape(organism, dX, dY)
        return False

    def collision(self, organism, dX, dY):
        if type(organism) != type(self) and not self.escape(organism, dX, dY):
            return
        else:
            super().collision(organism, dX, dY)