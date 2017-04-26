import tkinter as tk


class Window:
    """work with windows environment"""

    def __init__(self, title, win_w=800, win_h=480):
        self.master = tk.Tk()
        self.master.title(title)
        self.master.geometry('%dx%d' % (win_w, win_h))
        self.master.resizable(False, False)
        self.width = win_w
        self.height = win_h

    def run(self):
        """activate tkinter's loop"""
        self.master.mainloop()

    def center(self):
        """move window 2 center of screen
        (have not tested with few screens)"""
        self.master.update_idletasks()
        w = self.master.winfo_screenwidth()   # screen's width
        h = self.master.winfo_screenheight()  # screen's h8
        x = int((w - self.width) / 2)
        y = int((h - self.height) / 2)
        self.master.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))

