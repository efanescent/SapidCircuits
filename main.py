from Window import *
from World import *


if __name__ != '__main__': quit()

mainwin = Window('Ordinary Circuits')
mainwin.center()

world = World(mainwin.master)

mainwin.run()