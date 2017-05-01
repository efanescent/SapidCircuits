
class GameRenderer:
    """basic renderer"""
    def drawLine(self, xs, ys, xe, ye, color): pass
    def drawRect(self, xs, ys, xe, ye, color): pass
    def fillRect(self, xs, ys, xe, ye, color): pass
    def drawString(self, x, y, text, color): pass

class CanvasRenderer(GameRenderer):
    canvas = None

    def drawLine(self, xs, ys, xe, ye, color=None, **options):
        options['fill'] = color
        return self.canvas.create_line(xs, ys, xe, ye, **checkOptions(options))

    def drawRect(self, xs, ys, xe, ye, color=None, **options):
        options['outline'] = color
        return self.canvas.create_rectangle(xs, ys, xe, ye, **checkOptions(options))

    def fillRect(self, xs, ys, xe, ye, color=None, **options):
        return self.drawRect(xs, ys, xe, ye, fill=color, **options)

    def drawString(self, x, y, text, color=None, **options):
        options['fill'] = color
        return self.canvas.create_text(x, y, text=text, **checkOptions(options))

    def setCanvas(self, canvas):
        self.canvas = canvas


def checkOptions(options):
    """remove all elements eq None from dict"""
    result = dict()
    for key in options:
        if options[key] is not None:
            result[key] = options[key]
    return result
