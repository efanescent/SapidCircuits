import tkinter as tk
from Utils import *


class World:
    """class that contains 'in-window' logic, canvas, etc"""

    def __init__(self, window, x, y):
        self.canvas = tk.Canvas(window, highlightthickness=0, bg='#FFF3A4')
        self.canvas.pack(side='top', fill='both', expand=True)

    def clear(self):
        """remove all elements from canvas"""
        self.canvas.delete('all')


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
