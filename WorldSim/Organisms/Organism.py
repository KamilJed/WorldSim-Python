from abc import abstractmethod, ABC


class Organism(ABC):

    def __init__(self, x, y, world, strength=None):
        self._posX = x
        self._posY = y
        self._world = world
        self._color = "red"
        self._initiative = 0
        self._alive = True
        self._grownUp = False
        self._special = False
        self._heracleumProof = False
        if strength is not None:
            self._strength = strength

    @property
    def strength(self):
        return self._strength

    @property
    def posX(self):
        return self._posX

    @property
    def posY(self):
        return self._posY

    def draw(self):
        if self._world.isHexWorld:
            pass
        else:
            width = int(self._world.worldView.cget("width"))
            height = int(self._world.worldView.cget("height"))
            field_width = width / self._world.worldSizeX
            field_height = height / self._world.worldSizeY
            xoffset = (width - (self._world.worldSizeX * field_width)) / 2
            yoffset = (height - (self._world.worldSizeY * field_height)) / 2
            x0 = xoffset + (self._posX * field_width)
            y0 = yoffset + (self._posY * field_height)
            x1 = x0 + field_width
            y1 = y0 + field_height
            self._world.worldView.create_rectangle(x0, y0, x1, y1, fill=self._color)

    def kill(self):
        self._alive = False

    @property
    def alive(self):
        return self._alive

    def deflectAttack(self, organism):
        return False

    @property
    def grownUp(self):
        return self._grownUp

    @property
    def initiative(self):
        return self._initiative

    @abstractmethod
    def action(self):
        return

    def collision(self, organism, dX, dY):

        import WorldSim.Organisms.Animals.Animal
        import WorldSim.Organisms.Plants.Plant

        if isinstance(organism, WorldSim.Organisms.Plants.Plant.Plant):
            self._strength += organism.boost()
            if organism.isPoisonous() and not self.special:
                self.kill()
                organism.kill()
                self._world.setMessage(self.getName() + " has been poisoned")
                return
            else:
                organism.kill()
                self._world.setMessage(self.getName() + " has eaten " + organism.getName())
                return

        elif isinstance(organism, WorldSim.Organisms.Animals.Animal.Animal):
            if organism.escape(self, dX, dY):
                self._world.setMessage(organism.getName() + " has escaped")
                return
            if organism.deflectAttack(self):
                self._posX -= dX
                self._posY -= dY
                self._world.setMessage(organism.getName() + " has deflected the attack")
                return

        if self._strength < organism.strength:
            self.kill()
            self._world.setMessage(organism.getName() + " killed " + self.getName())
        else:
            organism.kill()
            self._world.setMessage(self.getName() + " killed " + organism.getName())

    def growUp(self):
        self._grownUp = True

    @abstractmethod
    def clone(self, x, y):
        return

    @abstractmethod
    def getName(self):
        return

    @property
    def special(self):
        return self._special

    def getFlatOrganism(self):
        flat = ""
        flat += self.getName()
        flat += ' '
        flat += str(self._posX)
        flat += ' '
        flat += str(self._posY)
        flat += ' '
        flat += str(self._strength)
        return flat

    @property
    def heracleumProof(self):
        return self._heracleumProof
