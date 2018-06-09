from WorldSim.Organisms.Animals.Animal import Animal
from Lib import random


class Tortoise(Animal):

    __moveChance = 25
    __shieldPower = 5

    def __init__(self, x, y, world, strength=None):
        super().__init__(x, y, world, strength)
        self._initiative = 1
        if strength is None:
            self._strength = 2
        self._color = "magenta"

    def clone(self, x, y):
        return Tortoise(x, y, self._world)

    def getName(self):
        return "Tortoise"

    def action(self):
        if random.randrange(0, 100, 1) <= Tortoise.__moveChance:
            super().action()

    def deflectAttack(self, organism):
        return organism.strength < Tortoise.__shieldPower
