from WorldSim.Organisms.Animals.Animal import Animal


class CyberSheep(Animal):

    def __init__(self, x, y, world, strength=None):
        super().__init__(x, y, world, strength)
        self._initiative = 4
        if strength is None:
            self._strength = 11
        self._color = "#754200"
        self._heracleumProof = True

    def clone(self, x, y):
        return CyberSheep(x, y, self._world)

    def getName(self):
        return "CyberSheep"

    def collision(self, organism, dX, dY):
        import WorldSim.Organisms.Plants.HeracleumSosnowskyi

        if isinstance(organism, WorldSim.Organisms.Plants.HeracleumSosnowskyi.HeracleumSosnowskyi):
            organism.kill()
        else:
            super().collision(organism, dX, dY)

    def action(self):

        target = self.searchTarget()
        if target is None:
            self._color = "blue"
            super().action()
        else:
            self._color = "#754200"
            dX = 0
            dY = 0
            if self._posX - target.posX != 0:
                if self._posX > target.posX:
                    dX = -1
                else:
                    dX = 1
            if self._posY - target.posY != 0:
                if self._posY > target.posY:
                    dY = -1
                else:
                    dY = 1

            field = self._world.isEmpty(self._posX + dX, self._posY + dY)
            self._posX += dX
            self._posY += dY
            if field is not None and field.alive:
                self.collision(field, dX, dY)

    def searchTarget(self):
        targetList = self._world.getHeracleum()
        distance = float("inf")
        targetLock = None
        for target in targetList:
            if abs(self._posX - target.posX) + abs(self._posY - target.posY) < distance:
                targetLock = target
                distance = abs(self._posX - target.posX) + abs(self._posY - target.posY)
        return targetLock



