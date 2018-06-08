from WorldSim.Worlds.World import World


class SquareWorld(World):

    def __init__(self, world_view, sizeX, sizeY):
        super().__init__(world_view, sizeX, sizeY)
        width = int(self._worldView.cget("width"))
        height = int(self._worldView.cget("height"))
        self._fieldWidth = width / self._worldSizeX
        self._fieldHeight = height / self._worldSizeY
        self._xOffset = (width - (self._worldSizeX * self._fieldWidth)) / 2
        self._yOffset = (height - (self._worldSizeY * self._fieldHeight)) / 2

    def drawWorld(self):
        for i in range(self._worldSizeY):
            for j in range(self._worldSizeX):
                x0 = self._xOffset + (j * self._fieldWidth)
                y0 = self._yOffset + (i * self._fieldHeight)
                x1 = x0 + self._fieldWidth
                y1 = y0 + self._fieldHeight
                self._worldView.create_rectangle(x0, y0, x1, y1, fill="white")

        for org in self._orgQueue:
            org.draw()

    def changeSize(self, sizeX, sizeY):
        super().changeSize(sizeX, sizeY)
        width = int(self._worldView.cget("width"))
        height = int(self._worldView.cget("height"))
        self._fieldWidth = width / self._worldSizeX
        self._fieldHeight = height / self._worldSizeY
        self._xOffset = (width - (self._worldSizeX * self._fieldWidth)) / 2
        self._yOffset = (height - (self._worldSizeY * self._fieldHeight)) / 2
        self.drawWorld()
