"""
Name: Jessica Andrews
threeDoorGame.py

Problem: creates a class with a clickable button
"""
from button import Button
from random import randint
from graphics import GraphWin, Rectangle, Point, Text

def create_message(x,y,message):
    message = Text(Point(x,y),message)
    return message
def make_rectangle(x1, y1, x2, y2):
    rectangle = Rectangle(Point(x1, y1),Point(x2, y2))
    return rectangle

def make_button(rectangle,label):
    buttons = Button(rectangle, label)
    return buttons


def check_button(door1,door2,door3):
    button_hit = bool(door1 or door2 or door3)
    return button_hit

def find_click(hit1,hit2,door1,door2,door3):
    if hit1:
        clicked = door1
    elif hit2:
        clicked = door2
    else:
        clicked = door3
    return clicked

def message_draw(mess1,mess2,win):
    mess1.draw(win)
    mess2.draw(win)
    return mess1, mess2

def winning_door(num,door1,door2,door3):
    if num == 1:
        winning = door1
    elif num == 2:
        winning = door2
    else:
        winning = door3
    return winning

def draw_label(rectangle,label,win):
    center = rectangle.getCenter()
    draw_text = Text(center,label)
    draw_text.draw(win)
    return draw_text

def new_screen(win_cent, clicked_cent, clicked , winning_door, win):
    if win_cent == clicked_cent:
        clicked.color_button("green")
        mess1 = create_message(10,15,"You Win!")
        mess2  = create_message(10,2,"Click to Close")
    else:
        clicked.color_button("red")
        mess1 = create_message(10,15,"sorry! That's wrong!")
        mess2 = create_message(10,2,"The correct door is {0}".format(winning_door.get_label()))
    clicked.draw(win)
    message_draw(mess1,mess2,win)


def main():
    win = GraphWin("Three Door Game", 400, 300)
    win.setCoords(0, 0, 20, 20)
    # creating rectangle to get centers
    rect1 = make_rectangle(2,10,6,12)
    rect2 = make_rectangle(8,10,12,12)
    rect3 = make_rectangle(14,10,18,12)
    # creating messages
    intro = create_message(10,15,"Pick a door!")
    # creating objects
    door1 = make_button(rect1,"Door1")
    door2 = make_button(rect2,"Door2")
    door3 = make_button(rect3,"Door3")
    # drawing objects
    door1.draw(win)
    door2.draw(win)
    door3.draw(win)
    #making labels
    intro.draw(win)
    draw_label(rect1,"Door1",win)
    draw_label(rect2,"Door2",win)
    draw_label(rect3,"Door3",win)
    # setting initial boolean
    hit = False
    hit_button1 = False
    hit_button2 = False

    while not hit:
        click = win.getMouse()
        hit_button1 = door1.is_clicked(click)
        hit_button2 = door2.is_clicked(click)
        hit_button3 = door3.is_clicked(click)
        hit = check_button(hit_button1,hit_button2,hit_button3)

    clicked_door = find_click(hit_button1,hit_button2,door1,door2,door3)
    clicked_door.undraw()
    intro.undraw()
    rando = randint(0,2)
    winner = winning_door(rando,door1,door2,door3)
    w_center = winner.get_center()
    c_center = clicked_door.get_center()
    new_screen(w_center,c_center,clicked_door,winner,win)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()