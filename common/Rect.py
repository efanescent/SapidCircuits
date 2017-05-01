
class Rect:
    def __init__(self, i_left, i_top, i_right, i_bottom):
        self.left = i_left
        self.top = i_top
        self.right = i_right
        self.bottom = i_bottom

    def contains(self, x, y):
        """check if point in rectangle"""
        xside = self.left <= x < self.right
        yside = self.top <= y < self.bottom
        return xside and yside

    def height(self):
        return self.bottom - self.top

    def width(self):
        return self.right - self.left