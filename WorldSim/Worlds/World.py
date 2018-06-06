from abc import abstractmethod, ABC


class World(ABC):

    def __init__(self, world_view):
        self.worldView = world_view
        self.worldSizeX = 20
        self.worldSizeY = 20
        width = int(world_view.cget("width"))
        height = int(world_view.cget("height"))
        self.fieldWidth = width / self.worldSizeX
        self.fieldHeight = height / self.worldSizeY
        self.xOffset = (width - (self.worldSizeX * self.fieldWidth)) / 2
        self.yOffset = (height - (self.worldSizeY * self.fieldHeight)) / 2

    @abstractmethod
    def draw_world(self):
        for i in range(self.worldSizeY):
            for j in range(self.worldSizeX):
                x0 = self.xOffset + (j * self.fieldWidth)
                y0 = self.yOffset + (i * self.fieldHeight)
                x1 = x0 + self.fieldWidth
                y1 = y0 + self.fieldHeight
                self.worldView.create_rectangle(x0, y0, x1, y1)

