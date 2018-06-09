from WorldSim.Organisms.Animals.Animal import Animal
from abc import ABC


class Escaper(Animal, ABC):

    def __init__(self, x, y, world, strength=None):
        super().__init__(x, y, world, strength)

    def escape(self, organism, dX, dY):
        maxX = self._world.worldSizeX
        maxY = self._world.worldSizeY

        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if self._posY + i < 0 or self._posY + i >= maxY:
                    break
                if 0 <= self._posX + j < maxX and self._world.isEmpty(self._posX + j, self._posY + i) is None:
                    self._posX += j
                    self._posY += i
                    return True
        return False
