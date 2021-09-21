"""
Name: <your name goes here – first and last>
<Lab4>.py

problem: PRoblems in lab 4
Certification of authenticity: I coordinated with Lesly and Katie
"""

from graphics import *
import math

def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move Square")
    instructions.draw(win)



    # builds a circle
    shape = Rectangle(Point(50, 50),Point(20,20))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of circle
        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape2 = shape.clone()
        shape2.draw(win)
        shape.move(dx, dy)

    instructions.undraw()
    newInstruction = Text(inst_pt, "Click to end program")
    newInstruction.draw(win)


    win.getMouse()
    win.close()



def rectangle():



    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """
    pass
    width = 400
    height = 400
    win = GraphWin("Draw a Rectangle", width, height)
    directions = Text(Point(200,350), "Draw a Rectangle")
    directions.draw(win)
    p1 = win.getMouse()
    p2 = win.getMouse()
    shape = Rectangle(p1,p2)
    shape.draw(win)

    varX = p1.getX()
    varY = p1.getY()
    var2X = p2.getX()
    var2Y = p2.getY()
    print(varX)
    print(varY)
    print(var2X)
    print(var2Y)

    length = abs(var2X - varX)
    height = abs(var2Y- varY)

    par = (length + height) * 2
    area = length * height
    print(par)
    print(area)

    directions.setText("Click to close")
    win.getMouse()

def circle():
    width = 400
    height = 400
    win = GraphWin("Draw a Circle", width, height)

    c = win.getMouse()
    r = win.getMouse()

    center = c.getX()
    center2 = c.getY()
    outer = r.getX()
    outer2 = r.getY()

    radius = math.sqrt((outer - center)**2 + (outer2 - center2)**2)
    coolCirc = Circle(c,radius)
    coolCirc.draw(win)
    radiusMes = Text(Point(200,10),radius)
    radiusMes.draw(win)
    closeProg = Text(Point(200,350),"Click to Close Program")
    closeProg.draw(win)

    win.getMouse()

# sorry brain empty
def pi():
    n = eval(input("How many terms will you want to sum"))

        add = 0
        number = eval(input("What will be your upper bound number?:"))
        for num in range(3, number + 1, 3):
            add = num + add
            print(num)
        print("the sum of these are:", add)


def main():
    squares()
    rectangle()
    circle()
    # pi2()


main()
