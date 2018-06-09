from WorldSim.Organisms.Organism import Organism
from abc import ABC
from Lib import random


class Plant(Organism, ABC):

    def __init__(self, x, y, world, strength=None):
        super().__init__(x, y, world, strength)
        self._poisonous = False
        self._boost = 0

    def action(self):
        if random.randrange(0, 100, 1) < 20:
            maxX = self._world.worldSizeX
            maxY = self._world.worldSizeY

            for i in range(-1, 1, 1):
                for j in range(-1, 1, 1):
                    if self._posY + i < 0 or self._posY + i >= maxY:
                        break
                    if (self._posX + j >= 0) and (self._posX + j < maxX) and self._world.isEmpty(self._posX + j, self._posY + i) is None:
                        self._world.addOrganism(self.clone(self._posX + j, self._posY + i))
                        self._world.setMessage(self.getName() + " has grown")
                        return

    @property
    def boost(self):
        return self._boost

    def isPoisonous(self):
        return self._poisonous