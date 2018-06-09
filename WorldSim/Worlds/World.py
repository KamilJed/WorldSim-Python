from abc import abstractmethod, ABC
from Lib import random
from tkinter.filedialog import *
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
from WorldSim.Organisms.Animals.CyberSheep import CyberSheep


class World(ABC):

    def __init__(self, world_view, sizeX, sizeY, label):
        self._worldView = world_view
        self._worldSizeX = sizeX
        self._worldSizeY = sizeY
        self._orgQueue = []
        self._isHexWorld = False
        self._human = None
        self._msgCount = 0
        self._textLabel = label
        self.cyberTest = True
        self.initWorld()

    @abstractmethod
    def drawWorld(self):
        pass

    def initWorld(self):
        for i in range(self._worldSizeY):
            for j in range(self._worldSizeX):
                character = random.randrange(0, 40, 1)

                # if character == 0:
                #     self.addOrganism(Sheep(j, i, self))
                # elif character == 1:
                #     self.addOrganism(Wolf(j, i, self))
                # elif character == 2:
                #     self.addOrganism(Grass(j, i, self))
                # elif character == 3:
                #     self.addOrganism(Guarana(j, i, self))
                # elif character == 4:
                #     self.addOrganism(Dandelion(j, i, self))
                # elif character == 5:
                #     self.addOrganism(DeadlyNightsahde(j, i, self))
                # elif character == 6:
                #     self.addOrganism(Antelope(j, i, self))
                # elif character == 7:
                #     self.addOrganism(Fox(j, i, self))
                # elif character == 8:
                #     self.addOrganism(Tortoise(j, i, self))
                # elif character == 9:
                #     self.addOrganism(HeracleumSosnowskyi(j, i, self))
                # elif character == 10:
                #     if self._human is None:
                #         self.addOrganism(Human(j, i, self))
                # elif character == 11:
                #     self.addOrganism(CyberSheep(j, i, self))

                if character == 0 or character == 3:
                    self.addOrganism(HeracleumSosnowskyi(j, i, self))
                elif character == 11 and self.cyberTest:
                    self.addOrganism(CyberSheep(j, i, self))
                    self.cyberTest = False

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
        self._textLabel['text'] = ""
        self._msgCount = 0
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
        self.cyberTest = True
        self._worldSizeX = sizeX
        self._worldSizeY = sizeY
        self._orgQueue = []
        self._worldView.delete("all")
        self.initWorld()
        self.drawWorld()

    def setHuman(self, human):
        self._human = human

    def killHuman(self):
        self._human = None

    def getHeracleum(self):
        heracleum = [org for org in self._orgQueue if isinstance(org, HeracleumSosnowskyi) and org.alive]
        return heracleum

    def setMessage(self, msg):
        if self._msgCount < 3:
            message = self._textLabel['text']
            message += msg + '\n'
            self._textLabel['text'] = message
            self._msgCount += 1

    def saveWorld(self):
        saveFile = asksaveasfile()
        saveFile.write(str(self._worldSizeX) + '\n')
        saveFile.write(str(self._worldSizeY) + '\n')
        for org in self._orgQueue:
            saveFile.write(org.getFlatOrganism() + '\n')
        saveFile.close()

    def loadWorld(self):
        self._human = None
        self._orgQueue = []
        self._worldView.delete("all")
        loadFile = askopenfile()
        self._worldSizeX = int(loadFile.readline())
        self._worldSizeY = int(loadFile.readline())
        for flatOrganism in loadFile:
            flatList = flatOrganism.split(' ')
            self.deflatOrganism(flatList)

        loadFile.close()
        self.drawWorld()

    def deflatOrganism(self, flatOrganism):
        name = flatOrganism[0]
        if name == "Human":
            self.addOrganism(Human(int(flatOrganism[1]), int(flatOrganism[2]), self, int(flatOrganism[3]),
                                   bool(flatOrganism[4]), int(flatOrganism[5])))
        elif name == "Sheep":
            self.addOrganism(Sheep(int(flatOrganism[1]), int(flatOrganism[2]), self, int(flatOrganism[3])))
        elif name == "Wolf":
            self.addOrganism(Wolf(int(flatOrganism[1]), int(flatOrganism[2]), self, int(flatOrganism[3])))
        elif name == "Grass":
            self.addOrganism(Grass(int(flatOrganism[1]), int(flatOrganism[2]), self, int(flatOrganism[3])))
        elif name == "Guarana":
            self.addOrganism(Guarana(int(flatOrganism[1]), int(flatOrganism[2]), self, int(flatOrganism[3])))
        elif name == "Dandelion":
            self.addOrganism(Dandelion(int(flatOrganism[1]), int(flatOrganism[2]), self, int(flatOrganism[3])))
        elif name == "DeadlyNightshade":
            self.addOrganism(DeadlyNightsahde(int(flatOrganism[1]), int(flatOrganism[2]), self, int(flatOrganism[3])))
        elif name == "Antelope":
            self.addOrganism(Antelope(int(flatOrganism[1]), int(flatOrganism[2]), self, int(flatOrganism[3])))
        elif name == "Fox":
            self.addOrganism(Fox(int(flatOrganism[1]), int(flatOrganism[2]), self, int(flatOrganism[3])))
        elif name == "Tortoise":
            self.addOrganism(Tortoise(int(flatOrganism[1]), int(flatOrganism[2]), self, int(flatOrganism[3])))
        elif name == "HeracleumSosnowskyi":
            self.addOrganism(HeracleumSosnowskyi(int(flatOrganism[1]), int(flatOrganism[2]), self, int(flatOrganism[3])))
        elif name == "CyberSheep":
            self.addOrganism(CyberSheep(int(flatOrganism[1]), int(flatOrganism[2]), self, int(flatOrganism[3])))

    @abstractmethod
    def addOnClick(self, organismName, x, y):
        return

    def createOrganism(self, name, x, y):
        if name == "Sheep":
            return Sheep(x, y, self)
        elif name == "Wolf":
            return Wolf(x, y, self)
        elif name == "Grass":
            return Grass(x, y, self)
        elif name == "Guarana":
            return Guarana(x, y, self)
        elif name == "Dandelion":
            return Dandelion(x, y, self)
        elif name == "DeadlyNightshade":
            return DeadlyNightsahde(x, y, self)
        elif name == "Antelope":
            return Antelope(x, y, self)
        elif name == "Fox":
            return Fox(x, y, self)
        elif name == "Tortoise":
            return Tortoise(x, y, self)
        elif name == "HeracleumSosnowskyi":
            return HeracleumSosnowskyi(x, y, self)
        elif name == "CyberSheep":
            return CyberSheep(x, y, self)