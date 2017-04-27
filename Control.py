# here detecting 'n' handling events...
# with keyboard 'n' mouse

import World

def pressed(key):
    """listener 4 keyboard pressing"""

    # zoom in
    if key.char == 'q':
        if World.scale_() - 2 > 0:
            World.scale_(-2)
            World.draw()
    # zoom out
    elif key.char == 'e':
        World.scale_(2)
        World.draw()
    # move view up
    if key.char == 'w':
        World.move_view(y=-1)
    # move view left
    elif key.char == 'a':
        World.move_view(x=-1)
    # move view down
    elif key.char == 's':
        World.move_view(y=1)
    # move view right
    elif key.char == 'd':
        World.move_view(x=1)