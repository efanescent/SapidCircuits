import World
import Control
from Window import *
from World import Field

mainwin = Window('Sapid Circuits')
mainwin.center()

World.init(mainwin.master, 4)
field = Field(200, 150, 10, 10)
World.set_field(field)
World.draw()

mainwin.run()