from Window import *
from World import *


if __name__ != '__main__': quit()

mainwin = Window('Sapid Circuits')
mainwin.center()

world = World(mainwin.master, 0, 0)

mainwin.run()