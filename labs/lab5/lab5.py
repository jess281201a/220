"""
Name: <Jessica Andrews>
lab5.py

Problem: Lab 5 problems of the week
"""
import math
from graphics import *

def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()

def triangle():

    # variable declaration
    pass
    width = 500
    height = 500
    window = GraphWin("Draw the triangle", width, height)
    message = Text(Point(width/2, height-10), "Click 3 points to draw a triangle")
    message.draw(window)
    point1 = window.getMouse()
    point2 = window.getMouse()
    point3 = window.getMouse()
    triangle1 = Polygon(point1, point2, point3)
    triangle1.draw(window)

    # point declaration
    varX1 = point1.getX()
    varY1 = point1.getY()
    varX2 = point2.getX()
    varY2 = point3.getY()
    varX3 = point3.getX()
    varY3 = point3.getY()

    length1 = abs(varX2) - abs(varX1)
    length2 = abs(varX1) - abs(varX3)
    length3 = abs(varX3) - abs(varX2)
    height1 = abs(varY2) - abs(varY1)
    height2 = abs(varY3) - abs(varY1)
    height3 = abs(varY3) - abs(varY2)

    # arithmatic
    sideA = math.sqrt(abs(length1**2 + height1**2))
    sideB = math.sqrt(abs(length2**2 + height2**2))
    sideC = math.sqrt(abs(length3**2 + height3**2))
    side = (sideA+sideB+sideC)/2
    area = math.sqrt(abs(side*(side-sideA))*((side-sideB)*(side-sideC)))
    perimeter = round(sideA + sideB + sideC,3)

    perimeterText = Text(Point(200, 300), "The perimeter is:")
    areaText = Text(Point(300, 300), "The Area is:")
    aText = Text(Point(300,350),area)
    pText = Text(Point(200,350), perimeter)
    pText.draw(window)
    aText.draw(window)


    perimeterText.draw(window)
    areaText.draw(window)

    window.getMouse()
    window.close()


# triangle()

def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''


    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_text_pt.move(0,30)
    redText = Entry(red_text_pt,5)
    redText.setText("0-255")
    redText.draw(win)



    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_text_pt.move(0,30)
    greenText = Entry(green_text_pt,5)
    greenText.setText("0-255")
    greenText.draw(win)



    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_text_pt.move(0,30)
    blueText = Entry(blue_text_pt,5)
    blueText.setText("0-255")
    blueText.draw(win)


    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for n in range (0,5):
        win.getMouse()
        blue = blueText.getText()
        green = greenText.getText()
        red = redText.getText()
        colour = color_rgb(eval(red), eval(green), eval(blue))
        shape.setFill(colour)



    # Wait for another click to exit
    win.getMouse()
    win.close()

color_shape()

def process_string():
    temp = 0
    stringInput = input("Please enter your string")
    print(stringInput[0])
    value = len(stringInput)
    print(stringInput[value - 1])
    print(stringInput[1:4])
    print(stringInput[0]+stringInput[value-1])
    for n in range (10):
        print(stringInput[0:3])
    for n in range(value):
        print(stringInput[n])
    print(value)


process_string()

def process_list():

    pt = Point(5,10)
    values = [5, "hi",2.5,"there",pt,"7.2"]
    val = len(values)
    ind = values.index()
    x = [ind-4]+[ind-2]
    print(x)
    x = [ind-5]+[ind-3]
    print(x)
    x = [ind-4]
    print(x*3)
    x = [ind-2]+[ind-3]+[ind-1]
    print(x)
    x = [ind-4]+[ind-2]+[ind-4]
    print(x)
    x = [ind - 3]+[ind-5]+[ind]
    print(x)
    x = val
    print(x)

process_list()
def main():
    # target()
    # triangle()
    # color_shape()
    pass


main()


