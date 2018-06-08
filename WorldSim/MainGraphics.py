from tkinter import *
from WorldSim.Worlds import SquareWorld


class MainWindow:

    def __init__(self):
        self.__mainWindow = Tk()
        self.__mainWindow.resizable(False, False)

        self.__worldView = Canvas(self.__mainWindow, height=700, width=700, border=1, bg="white", relief=SUNKEN)
        self.__worldView.grid(row=0, columnspan=2)
        self.__world = SquareWorld.SquareWorld(self.__worldView, 20, 20)
        self.__worldView.bind("<Left>", self.__world.leftCatch)
        self.__worldView.bind("<Up>", self.__world.upCatch)
        self.__worldView.bind("<Right>", self.__world.rightCatch)
        self.__worldView.bind("<Down>", self.__world.downCatch)
        self.__worldView.bind("e", self.__world.eCatch)
        self.__worldView.focus_set()

        self.__messagesOutput = Label(self.__mainWindow, text="Press new turn to begin")
        self.__messagesOutput.grid(row=4, column=0)

        self.__newTurnButton = Button(self.__mainWindow, text="New Turn", width=40, command=self.__world.newTurn)
        self.__newTurnButton.grid(row=4, column=1, columnspan=2)

        self.__xSizeSpinner = Spinbox(self.__mainWindow, from_=2, to=50)
        self.__xSizeSpinner.grid(row=0, column=2)
        self.__ySizeSpinner = Spinbox(self.__mainWindow, from_=2, to=50)
        self.__ySizeSpinner.grid(row=0, column=3)

        self.__setWorldSizeButton = Button(self.__mainWindow, text="Set world size", width=30, command=self.__changeSize)
        self.__setWorldSizeButton.grid(row=1, column=2, columnspan=2)

        self.__organismChoosen = StringVar(self.__mainWindow, "Antelope")
        organisms = ["Antelope", "Fox", "Sheep", "Cyber-Sheep", "Tortoise", "Wolf", "Dandelion", "DeadlyNightshade",
                     "Grass", "Guarana", "HeacleumSosnowskyi"]
        self.__organismChooser = OptionMenu(self.__mainWindow, self.__organismChoosen, *organisms)
        self.__organismChooser.grid(row=0, column=4)
        self.__world.drawWorld()
        self.__mainWindow.mainloop()

    def __changeSize(self):
        self.__world.changeSize(int(self.__xSizeSpinner.get()), int(self.__ySizeSpinner.get()))


window = MainWindow()

