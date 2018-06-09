from WorldSim.Organisms.Organism import Organism
from abc import ABC
from Lib import random


class Animal(Organism, ABC):

    def __init__(self, x, y, world, strength=None):
        super().__init__(x, y, world, strength)

    def action(self):
        dX = 0
        dY = 0

        if self._world.isHexWorld:
            pass
            #TODO
        else:
            dX = random.randrange(-1, 2, 1)
            if (self._posX + dX < 0) or (self._posX + dX >= self._world.worldSizeX):
                dX = 0

            dY = random.randrange(-1, 2, 1)
            if (self._posY + dY < 0) or (self._posY + dY >= self._world.worldSizeY):
                dY = 0

            field = None

            if dX != 0 or dY != 0:
                field = self._world.isEmpty(self._posX + dX, self._posY + dY)

            self._posX += dX
            self._posY += dY

            if field is not None and field.alive:
                self.collision(field, dX, dY)

    def collision(self, organism, dX, dY):
        if type(self) == type(organism):
            self._posX -= dX
            self._posY -= dY

            maxX = self._world.worldSizeX
            maxY = self._world.worldSizeY

            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if self._posY + i < 0 or self._posY + i >= maxY:
                        break
                    if (self._posX + j >= 0) and (self._posX + j < maxX) and self._world.isEmpty(self._posX + j, self._posY + i) is None:
                        self._world.addOrganism(self.clone(self._posX + j, self._posY + i))
                        self._world.setMessage(self.getName() + " has been born")
                        return
        else:
            super().collision(organism, dX, dY)

    def escape(self, organism, dX, dY):
        return False
