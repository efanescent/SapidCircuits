import Control
from tkinter.messagebox import showerror
from Window import *
from Utils import *

canvas, field, scale = None, None, None

def init(window, p_field=-1, p_scale=10):
    """using to init World with params"""
    global canvas, field, scale
    canvas = tk.Canvas(window, highlightthickness=0, bg='#FFF3A4')
    canvas.pack(side='top', fill='both', expand=True)
    field = p_field
    scale = p_scale

    # auto setting control
    try: set_control()
    except:
        showerror('Error', 'Control can\'t be set')


def set_field(p_field):
    """set up field in the world"""
    global field
    field = p_field

def clear():
    """remove all elements from canvas"""
    global canvas
    canvas.delete('all')

def scale_(*args, **kwargs):
    """universal function for set/get/change scale
    if arg is num - change scale
    if kwarg wiz index 'set' - set scale
    and then return current scale"""
    global scale
    for arg in args:
        if isinstance(scale, (int, float)):
            scale += arg
    for key in kwargs:
        if key == 'set':
            scale = kwargs[key]
    return scale

def draw():
    global canvas, field, scale
    if field == -1: return False

    # possibly this is bad idea... idk
    clear()

    # redraw empty tiles
    cx, cy = field.x, field.y
    for col in range(int(field.height)):
        for row in range(int(field.width)):
            canvas.create_rectangle(cx, cy, cx+1000/scale, cy+1000/scale)
            cx += (1000/scale)
        cx = field.x
        cy += (1000/scale)

def set_control():
    """set control..."""
    canvas.master.bind_all('<Key>', Control.pressed)

def move_view(**kwargs):
    for key in kwargs:
        if key == 'x':
            canvas.xview_scroll(int(kwargs[key]), 'units')
        if key == 'y':
            canvas.yview_scroll(int(kwargs[key]), 'units')

class Field:
    """class contains tiles"""

    def __init__(self, sx, sy, width, height):
        self.x = sx  # start x
        self.y = sy  # start y
        # width 'n' height in units (f.e. 2x3 = 6units or tiles)
        self.width = width
        self.height = height
        self.tiles = dict()  # no tiles, excepting empty

    def add_tile(self, tx, ty, tile):
        """add tile in tiles container"""
        self.tiles[tile_xy2i(tx, ty)] = tile

    def get_tile(self, tx, ty):
        """return tile from tiles container"""
        try:
            return self.tiles[tile_xy2i(tx, ty)]
        except:
            return -1

    def is_empty_tile(self, tx, ty):
        """return bool - tile is empty"""
        try:
            self.tiles[tile_xy2i(tx, ty)]
        except:
            return True
        else:
            return False


class Tile:
    def __init__(self, Id):
        self.ID = Id