"""
Name: Jessica Andrews
greeting.py

Problem: Draw an animation of a heart with an arrow shot through it
I certify that this program is entirely my own work

"""
from graphics import GraphWin, Circle, Polygon, Point, Text, Line, color_rgb, time


def main():

    # window object creation
    win = GraphWin("Greeting", 500, 500)
    win.setCoords(0, 0, 20, 20)

    # heart creation
    left_h = Circle(Point(7.5, 14), 2.9)
    right_h = Circle(Point(12, 14), 2.9)
    base = Polygon(Point(4.9521, 12.53), Point(14.532, 12.5), Point(9.6, 6))
    message = Text(Point(9.8, 4), 'Happy Valentines Day!')

    # arrow building
    stem = Line(Point(2, 2), Point(6, 7))
    quiver = Line(Point(1.5, 2), Point(2, 2))
    quiv2 = Line(Point(2, 1), Point(2, 2.1))
    quiv3 = Line(Point(3.4, 3.8), Point(3.26, 2))
    quiv4 = Line(Point(1.9, 2.8), Point(3.6, 3.9))
    arrow = Polygon(Point(5, 7), Point(7, 8.2), Point(6, 6))

    # colour addition
    left_h.setFill(color_rgb(89, 13, 34))
    left_h.setOutline(color_rgb(89, 13, 34))
    right_h.setFill(color_rgb(89, 13, 34))
    right_h.setOutline(color_rgb(89, 13, 34))
    base.setFill(color_rgb(89, 13, 34))
    base.setOutline(color_rgb(89, 13, 34))
    arrow.setFill(color_rgb(216, 226, 220))

    # draw calls
    left_h.draw(win)
    right_h.draw(win)
    base.draw(win)
    stem.draw(win)
    quiver.draw(win)
    quiv2.draw(win)
    quiv3.draw(win)
    quiv4.draw(win)
    arrow.draw(win)
    message.draw(win)

    # for loop
    for _ in range(15):
        stem.move(3, 3)
        quiver.move(3, 3)
        quiv2.move(3, 3)
        quiv3.move(3, 3)
        quiv4.move(3, 3)
        arrow.move(3, 3)
        time.sleep(0.1)
    message.undraw()
    message2 = Text(Point(9.8, 4), 'Click to close!')
    message2.draw(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
