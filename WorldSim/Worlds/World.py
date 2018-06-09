from abc import abstractmethod, ABC
from Lib import random
from WorldSim.Organisms.Animals.Sheep import Sheep
from WorldSim.Organisms.Animals.Wolf import Wolf
from WorldSim.Organisms.Plants.Grass import Grass
from WorldSim.Organisms.Plants.Guarana import Guarana
from WorldSim.Organisms.Plants.Dandelion import Dandelion
from WorldSim.Organisms.Plants.DeadlyNightshade import DeadlyNightsahde
from WorldSim.Organisms.Animals.Antelope import Antelope
from WorldSim.Organisms.Animals.Fox import Fox
from WorldSim.Organisms.Animals.Tortoise import Tortoise
from WorldSim.Organisms.Plants.HeracleumSosnowskyi import HeracleumSosnowskyi
from WorldSim.Organisms.Animals.Human import Human


class World(ABC):

    def __init__(self, world_view, sizeX, sizeY):
        self._worldView = world_view
        self._worldSizeX = sizeX
        self._worldSizeY = sizeY
        self._orgQueue = []
        self._isHexWorld = False
        self._human = None
        self.initWorld()

    @abstractmethod
    def drawWorld(self):
        pass

    def initWorld(self):
        for i in range(self._worldSizeY):
            for j in range(self._worldSizeX):
                character = random.randrange(0, 40, 1)

                if character == 0:
                    self.addOrganism(Sheep(j, i, self))
                elif character == 1:
                    self.addOrganism(Wolf(j, i, self))
                elif character == 2:
                    self.addOrganism(Grass(j, i, self))
                elif character == 3:
                    self.addOrganism(Guarana(j, i, self))
                elif character == 4:
                    self.addOrganism(Dandelion(j, i, self))
                elif character == 5:
                    self.addOrganism(DeadlyNightsahde(j, i, self))
                elif character == 6:
                    self.addOrganism(Antelope(j, i, self))
                elif character == 7:
                    self.addOrganism(Fox(j, i, self))
                elif character == 8:
                    self.addOrganism(Tortoise(j, i, self))
                elif character == 9:
                    self.addOrganism(HeracleumSosnowskyi(j, i, self))
                elif character == 10:
                    if self._human is None:
                        self.addOrganism(Human(j, i, self))

    @property
    def worldView(self):
        return self._worldView

    @property
    def worldSizeX(self):
        return self._worldSizeX

    @property
    def worldSizeY(self):
        return self._worldSizeY

    @property
    def isHexWorld(self):
        return self._isHexWorld

    def isEmpty(self, x, y):
        for org in self._orgQueue:
            if org.posX == x and org.posY == y:
                return org
        return None

    def addOrganism(self, organism):
        self._orgQueue.append(organism)
        self._orgQueue = sorted(self._orgQueue, key=lambda org: org.initiative, reverse=True)

    def newTurn(self, event=None):
        self._worldView.delete("all")
        for org in self._orgQueue:
            if org.alive and org.grownUp:
                org.action()
            else:
                org.growUp()

        self._deleteOrganisms()
        self.drawWorld()
        if self._human is not None:
            self._human.abilityControl()

    def _deleteOrganisms(self):
        self._orgQueue[:] = [org for org in self._orgQueue if org.alive]

    def leftCatch(self, event):
        if self._human is not None:
            self._human.dX = -1

    def upCatch(self, event):
        if self._human is not None:
            self._human.dY = -1

    def rightCatch(self, event):
        if self._human is not None:
            self._human.dX = 1

    def downCatch(self, event):
        if self._human is not None:
            self._human.dY = 1

    def eCatch(self, event):
        if self._human is not None:
            self._human.turnAbility()

    def changeSize(self, sizeX, sizeY):
        self._human = None
        self._worldSizeX = sizeX
        self._worldSizeY = sizeY
        self._orgQueue = []
        self._worldView.delete("all")
        self.initWorld()

    def setHuman(self, human):
        self._human = human

    def killHuman(self):
        self._human = None