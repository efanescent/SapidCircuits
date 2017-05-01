from GameInstance import *
from Window import *
import tkinter as tk
import time

window = Window()
canvas = tk.Canvas(window, bg='yellow')
canvas.pack(side='top', fill='both', expand=1)

def run(tim):
    l1 = tim
    l2 = int(round(time.time() * 1000))
    f = .001 * (l2 - l1)
    print(l2 - l1)
    instance.update()
    FPSCounter.frame(f)
    window.after(10, run, l2)


renderer = CanvasRenderer()
renderer.setCanvas(canvas)
instance = GameInstance(renderer)


instance.draw()
run(int(round(time.time() * 1000)))
window.center()
window.mainloop()