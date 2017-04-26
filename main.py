from Window import *
from World import *


if __name__ != '__main__': quit()

mainwin = Window('Sapid Circuits')
mainwin.center()

world = World(mainwin.master)
field = Field(200, 150, 10, 10)
world.inject_field(field)
world.draw()


mainwin.run()