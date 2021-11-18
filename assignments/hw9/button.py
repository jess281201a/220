"""
Name: Jessica Andrews
button.py

Problem: creates a class with a clickable button
"""


class Button:
    def __init__(self, rectangle, label):
        self.shape = rectangle
        self.text = label

    def set_label(self, label):
        label = self.text
        string = label.getText()
        return string

    def get_label(self):
        return self.text

    def draw(self, win):
        self.shape.draw(win)


    def undraw(self):
        self.shape.undraw()

    def get_corner(self):
        rectangle = self.shape
        x1 = rectangle.getP1().getX()
        y1 = rectangle.getP1().getY()
        x2 = rectangle.getP2().getX()
        y2 = rectangle.getP2().getY()
        return x1, y1, x2, y2

    def get_center(self):
        rectangle = self.shape
        center = rectangle.getCenter
        return center

    def is_clicked(self, point):
        userX = point.getX()
        userY = point.getY()
        x1,y1,x2,y2 = self.get_corner()
        # check if point is inside window
        hit = bool(x1 <= userX <= x2 and y1 <= userY <= y2)
        return hit

    def color_button(self, colour):
        colour = str(colour)
        rectangle = self.shape
        rectangle.setFill(colour)