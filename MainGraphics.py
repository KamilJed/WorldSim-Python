from tkinter import *
from WorldSim import World


class MainWindow:
    mainWindow = Tk()
    mainWindow.resizable(False, False)

    worldView = Canvas(mainWindow, height=700, width=700, border=1, bg="white", relief=SUNKEN)
    worldView.grid(row=0, columnspan=2)
    world = World.World(worldView)

    messagesOutput = Label(mainWindow, text="Press new turn to begin")
    messagesOutput.grid(row=4, column=0)

    newTurnButton = Button(mainWindow, text="New Turn", width=40)
    newTurnButton.grid(row=4, column=1, columnspan=2)

    xSizeSpinner = Spinbox(mainWindow, from_=2, to=50)
    xSizeSpinner.grid(row=0, column=2)
    ySizeSpinner = Spinbox(mainWindow, from_=2, to=50)
    ySizeSpinner.grid(row=0, column=3)

    worldChoose = StringVar(mainWindow)
    squareWorldRadio = Radiobutton(mainWindow, text="Square Grid", variable=worldChoose, value="Square")
    squareWorldRadio.select()
    squareWorldRadio.grid(row=1, column=2)
    squareWorldRadio = Radiobutton(mainWindow, text="Hex Grid", variable=worldChoose, value="Hex")
    squareWorldRadio.grid(row=1, column=3)

    setWorldSizeButton = Button(mainWindow, text="Set world size", width=30)
    setWorldSizeButton.grid(row=2, column=2, columnspan=2)

    organismChoosen = StringVar(mainWindow, "Antelope")
    organisms = ["Antelope", "Fox", "Sheep", "Cyber-Sheep", "Tortoise", "Wolf", "Dandelion", "DeadlyNightshade",
                 "Grass", "Guarana", "HeacleumSosnowskyi"]
    organismChooser = OptionMenu(mainWindow, organismChoosen, *organisms)
    organismChooser.grid(row=0, column=4)

    def __init__(self):
        self.world.draw_world()
        self.mainWindow.mainloop()


window = MainWindow()

