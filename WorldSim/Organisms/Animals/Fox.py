from WorldSim.Organisms.Animals.Animal import Animal
from Lib import random


class Fox(Animal):

    def __init__(self, x, y, world, strength=None):
        super().__init__(x, y, world, strength)
        self._initiative = 7
        if strength is None:
            self._strength = 3
        self._color = "pink"

    def clone(self, x, y):
        return Fox(x, y, self._world)

    def getName(self):
        return "Fox"

    def action(self):
        maxX = self._world.worldSizeX
        maxY = self._world.worldSizeY

        i = random.randrange(-1, 2, 1)
        for a in range(0, 3):
            j = random.randrange(-1, 2, 1)
            for b in range(0, 3):
                if self._posY + i < 0 or self._posY + i >= maxY or (i == 0 and j == 0):
                    if ++j == 2:
                        j = -1
                    break
                if self._posX + j >= 0 and self._posX + j < maxX:
                    organism = self._world.isEmpty(self._posX + j, self._posY + i)

                    if organism is None:
                        self._posX += j
                        self._posY += i
                        return
                    elif organism.strength <= self._strength or type(organism) == type(self):
                        self._posX += j
                        self._posY += i
                        super().collision(organism, j, i)
                        return