from WorldSim.Organisms.Plants.Plant import Plant


class HeracleumSosnowskyi(Plant):

    def __init__(self, x, y, world, strength=None):
        super().__init__(x, y, world, strength)
        self._initiative = 0
        if strength is None:
            self._strength = 10
        self._color = "#888"
        self._poisonous = True

    def clone(self, x, y):
        return HeracleumSosnowskyi(x, y, self._world)

    def getName(self):
        return "HeracleumSosnowskyi"

    def action(self):
        import WorldSim.Organisms.Animals.Animal
        maxX = self._world.worldSizeX
        maxY = self._world.worldSizeY

        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if self._posY + i < 0 or self._posY + i >= maxY:
                    break
                if (self._posX + j >= 0) and (self._posX + j < maxX):
                    organism = self._world.isEmpty(self._posX + j, self._posY + i)

                    if isinstance(organism, WorldSim.Organisms.Animals.Animal.Animal):
                        if not organism.special and not organism.heracleumProof:
                            organism.kill()
