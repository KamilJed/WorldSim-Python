from WorldSim.Worlds.World import World


class SquareWorld(World):

    def __init__(self, world_view, sizeX, sizeY, label):
        super().__init__(world_view, sizeX, sizeY, label)

    def drawWorld(self):
        fieldWidth, fieldHeight, xOffset, yOffset = self.calculate()
        for i in range(self._worldSizeY):
            for j in range(self._worldSizeX):
                x0 = xOffset + (j * fieldWidth)
                y0 = yOffset + (i * fieldHeight)
                x1 = x0 + fieldWidth
                y1 = y0 + fieldHeight
                self._worldView.create_rectangle(x0, y0, x1, y1, fill="white")

        for org in self._orgQueue:
            org.draw()

    def calculate(self):
        width = int(self._worldView.cget("width"))
        height = int(self._worldView.cget("height"))
        fieldWidth = width / self._worldSizeX
        fieldHeight = height / self._worldSizeY
        xOffset = (width - (self._worldSizeX * fieldWidth)) / 2
        yOffset = (height - (self._worldSizeY * fieldHeight)) / 2
        return fieldWidth, fieldHeight, xOffset, yOffset

    def addOnClick(self, organismName, x, y):
        fieldWidth, fieldHeight, xOffset, yOffset = self.calculate()
        if x >= xOffset and y >= yOffset:
            column = int((x - xOffset) / fieldWidth)
            row = int((y - yOffset) / fieldHeight)

            if 0 <= column < self._worldSizeX and 0 <= row < self._worldSizeY:
                field = self.isEmpty(column, row)
                if field is None:
                    self.addOrganism(self.createOrganism(organismName, column, row))
                    self.drawWorld()
