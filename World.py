import tkinter as tk


class World:
    """class that contains canvas, 'world memory', etc"""

    def __init__(self, window):
        self.canvas = tk.Canvas(window, highlightthickness=0, bg='yellow')
        self.canvas.pack(side='top', fill='both', expand=True)

    def clear(self):
        """remove all elements from canvas"""
        self.canvas.delete('all')

