from tkinter import *
from graphics.GameRenderer import *

class Window(Tk):
    def __init__(self, width=800, height=480):
        Tk.__init__(self)
        self.geometry('%dx%d' % (width, height))
        self.resizable(*(0 for i in range(2)))  # lmao

    def center(self):
        """set window on the center"""
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        x = int((self.winfo_screenwidth() - w) / 2)
        y = int((self.winfo_screenheight() - h) / 2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))


if __name__ == '__main__':
    window = Window()
    window.center()
    canvas = Canvas(window, bg='yellow')
    canvas.pack(side=TOP, fill=BOTH, expand=1)
    renderer = CanvasRenderer()
    renderer.setCanvas(canvas)
    renderer.fillRect(0, 0, 200, 200, 'red', activedash=(4, 4))
    renderer.drawString(100, 100, 'Awesome awesome', 'red')
    window.mainloop()
