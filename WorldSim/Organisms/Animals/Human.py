from WorldSim.Organisms.Animals.Escaper import Escaper


class Human(Escaper):

    def __init__(self, x, y, world, strength=None, special=None, turns=None):
        super().__init__(x, y, world, strength)
        self._initiative = 4
        if strength is None:
            self._strength = 5
        if special is None:
            self._special = False
        else:
            self._special = special
        if turns is None:
            self._turnsRemaining = 0
        else:
            self._turnsRemaining = turns
        self._dX = 0
        self._dY = 0
        if self._special:
            self._color = "#7a1000"
        else:
            self._color = "red"
        world.setHuman(self)

    def clone(self, x, y):
        return Human(x, y, self._world)

    def getName(self):
        return "Human"

    def kill(self):
        super().kill()
        self._world.killHuman()

    def action(self):
        if 0 <= self._posY + self._dY < self._world.worldSizeY and 0 <= self._posX + self._dX < self._world.worldSizeX:

            field = self._world.isEmpty(self._posX + self._dX, self._posY + self._dY)
            self._posX += self._dX
            self._posY += self._dY
            if (self._dX != 0 or self._dY != 0) and field is not None:
                self.collision(field, self._dX, self._dY)

        self._dX = 0
        self._dY = 0

    @property
    def dX(self):
        return self._dX

    @dX.setter
    def dX(self, dX):
        self._dX = dX
        self._dY = 0

    @property
    def dY(self):
        return self._dY

    @dY.setter
    def dY(self, dY):
        self._dY = dY
        self._dX = 0

    def turnAbility(self):
        if self._turnsRemaining == 0:
            self._special = True
            self._turnsRemaining = 5
            self._color = "#7a1000"

    def escape(self, organism, dX, dY):
        import WorldSim.Organisms.Plants.Plant
        if isinstance(organism, WorldSim.Organisms.Plants.Plant.Plant):
            return False

        if self._special and organism.strength >= self._strength:
            return super().escape(organism, dX, dY)
        return False

    def getFlatOrganism(self):
        flat = super().getFlatOrganism()
        flat += ' '
        flat += str(self._special)
        flat += ' '
        flat += str(self._turnsRemaining)
        return flat

    def abilityControl(self):
        if self._turnsRemaining < 0:
            self._turnsRemaining += 1
        elif self._turnsRemaining != 0:
            self._turnsRemaining -= 1

        if self._turnsRemaining == 0 and self._special:
            self._turnsRemaining = -5
            self._special = False
            self._color = "red"

