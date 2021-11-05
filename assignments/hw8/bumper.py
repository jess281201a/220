"""
Name: Jessica Andrews
bumper.py

Problem: Creates 2 balls colliding on a window
"""
import time
from random import randint
from math import sqrt
from graphics import Circle, Point, GraphWin, color_rgb



def get_random(move_amount):
    move = randint(-move_amount, move_amount)
    return move


def did_collide(ball, ball2):
    # get centers
    # get X's
    ball_center_x = ball.getCenter().getX()
    ball2_center_x = ball2.getCenter().getX()
    # get Y's
    ball_center_y = ball.getCenter().getY()
    ball2_center_y = ball2.getCenter().getY()
    # get radius
    ball_radius = ball.getRadius()
    ball2_radius = ball2.getRadius()
    sub_x = ball2_center_x - ball_center_x
    sub_y = ball2_center_y - ball_center_y
    # equation
    sum_radi = ball2_radius + ball_radius
    distance = sqrt((sub_x**2) + (sub_y**2))
    if distance <= sum_radi:
        return True
    else:
        return False


def hit_vertical(ball, win):
    circle = ball.getCenter().getX()
    width = win.getWidth()
    radius = ball.getRadius()
    if (circle + radius) >= width or (circle - radius) <= 0:
        return True
    else:
        return False


def hit_horizontal(ball, win):
    height = win.getHeight()
    radius = ball.getRadius()
    circle = ball.getCenter().getY()
    if (circle + radius) >= height or (circle - radius) <= 0:
        return True
    else:
        return False


def get_random_color():
    colours = color_rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    return colours


def draw_circle(win):
    ball = Circle(Point(randint(200, 300), randint(200, 400)), randint(30, 50))
    ball.setFill(get_random_color())
    ball.draw(win)
    return ball



def main():
    win = GraphWin("Bumper Cars", randint(400, 800), randint(400, 800))
    ball = draw_circle(win)
    ball2 = draw_circle(win)
    win.setBackground(get_random_color())
    pos = 10
    x_one = get_random(pos)
    x_two = get_random(pos)
    y_one = get_random(pos)
    y_two = get_random(pos)
    ball.move(x_one, y_one)
    time.sleep(.01)
    ball2.move(x_two, y_two)
    time.sleep(.01)
    while not(win.checkMouse()):
        ball.move(x_one, y_one)
        time.sleep(.01)
        ball2.move(x_two, y_two)
        time.sleep(.01)
        if hit_vertical(ball, win) is True:
            x_one = x_one * -1
        if hit_horizontal(ball, win) is True:
            y_one = y_one * -1
        if hit_vertical(ball2, win) is True:
            x_two = x_two * -1
        if hit_horizontal(ball2, win) is True:
            y_two = x_two * -1
        if did_collide(ball, ball2) is True:
            x_one = x_one * -1
            y_one = y_one * -1
            x_two = x_two * -1
            y_two = y_two * -1
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
