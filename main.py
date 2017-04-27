import World as World
from Window import *
from World import Field


def pressed(key):
    # zoom up
    if key.char == 'q':
        World.scale_(.2)
        World.draw()
    # zoom down
    elif key.char == 'e':
        World.scale_(-.2)
        World.draw()
    print(World.scale_())


mainwin = Window('Sapid Circuits')
mainwin.center()

World.init(mainwin.master, 4)
field = Field(200, 150, 10, 10)
World.set_field(field)
World.draw()

mainwin.master.bind_all('<Key>', pressed)

mainwin.run()