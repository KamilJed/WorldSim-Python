from tkinter import *
from WorldSim.Worlds import SquareWorld


class MainWindow:

    def __init__(self):
        self.__mainWindow = Tk()
        self.__mainWindow.resizable(False, False)

        self.__worldView = Canvas(self.__mainWindow, height=650, width=650, border=1, bg="white", relief=GROOVE)
        self.__worldView.grid(row=0, columnspan=10, rowspan=10)

        self.__messagesOutput = Label(self.__mainWindow, text="Press new turn to begin", height=6, width=92, bg="white", fg="green", relief=GROOVE)
        self.__messagesOutput.grid(row=10, column=0)

        self.__world = SquareWorld.SquareWorld(self.__worldView, 20, 20, self.__messagesOutput)
        self.__worldView.bind("<Left>", self.__world.leftCatch)
        self.__worldView.bind("<Up>", self.__world.upCatch)
        self.__worldView.bind("<Right>", self.__world.rightCatch)
        self.__worldView.bind("<Down>", self.__world.downCatch)
        self.__worldView.bind("e", self.__world.eCatch)
        self.__worldView.bind("<space>", self.__world.newTurn)
        self.__worldView.bind("<Button-1>", self.__addOrganism)
        self.__worldView.focus_set()

        self.__newTurnButton = Button(self.__mainWindow, text="New Turn", width=40, command=self.__world.newTurn)
        self.__newTurnButton.grid(row=6, column=12, columnspan=2)

        self.__xSizeSpinner = Spinbox(self.__mainWindow, from_=2, to=50, value=20)
        self.__xSizeSpinner.grid(row=2, column=12)
        self.__ySizeSpinner = Spinbox(self.__mainWindow, from_=2, to=50, value=20)
        self.__ySizeSpinner.grid(row=2, column=13)

        self.__setWorldSizeButton = Button(self.__mainWindow, text="Set world size", width=30, command=self.__changeSize)
        self.__setWorldSizeButton.grid(row=3, column=12, columnspan=2)

        self.__saveWorldButton = Button(self.__mainWindow, text="Save", width=30, command=self.__world.saveWorld)
        self.__saveWorldButton.grid(row=4, column=12)
        self.__loadWorldButton = Button(self.__mainWindow, text="Load", width=30, command=self.__world.loadWorld)
        self.__loadWorldButton.grid(row=4, column=13)

        self.__organismChoosen = StringVar(self.__mainWindow, "Antelope")
        organisms = ["Antelope", "Fox", "Sheep", "CyberSheep", "Tortoise", "Wolf", "Dandelion", "DeadlyNightshade",
                     "Grass", "Guarana", "HeracleumSosnowskyi"]
        self.__organismChooser = OptionMenu(self.__mainWindow, self.__organismChoosen, *organisms)
        self.__organismChooser.grid(row=0, column=12)
        self.__world.drawWorld()
        self.__mainWindow.mainloop()

    def __changeSize(self):
        self.__world.changeSize(int(self.__xSizeSpinner.get()), int(self.__ySizeSpinner.get()))
        self.__worldView.focus_set()

    def __addOrganism(self, event):
        organism = self.__organismChoosen.get()
        self.__world.addOnClick(organism, event.x, event.y)


window = MainWindow()

