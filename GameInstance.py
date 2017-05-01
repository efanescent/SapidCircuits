from graphics.GameRenderer import *
import FPSCounter

class GameInstance:

    def __init__(self, gameRenderer):
        self.renderer = gameRenderer
        self.surfaceFrame = None

    def draw(self):
        str = 'FPS: %d' % FPSCounter.getFps()
        self.fpsstr = self.renderer.drawString(10, 10, str, 'red', anchor='nw')

    def update(self):
        str = 'FPS: %d' % FPSCounter.getFps()
        self.renderer.canvas.itemconfig(self.fpsstr, text=str)