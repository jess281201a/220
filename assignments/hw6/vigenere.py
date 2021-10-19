"""
Name: Jessica Andrews
vigenere.py

Problem: Asks user for input of a secret message and keyword, runs the vigenere cypher and outputs the answer
I certify that this program is entirely my own work
"""
from graphics import *


def format_message(secret_message):
    secret_message = secret_message.upper()
    secret_message = secret_message.replace(" ", "")
    return secret_message


def code(message, keyword):
    secret_message = format_message(message)
    word = format_message(keyword)
    key = []
    for i in range(len(secret_message)):
        pos = secret_message[i]
        loop = i % len(word)
        convert = ord(pos) - 65
        word_convert = ord(word[loop]) - 65
        encode = chr(((convert + word_convert) % 26) + 65)
        key.append(encode)
    text = "".join(key)
    return text


def text_input(textbox_input):
    string = textbox_input.getText()
    return string


def main():
    win = GraphWin("Vigenere", 400, 300)
    win.setCoords(0, 0, 10, 10)

    mess1 = Text(Point(2, 8), "Message to code")
    mess1.draw(win)
    mess2 = Text(Point(2.2, 7), "Enter Keyword")
    mess2.draw(win)

    button = Rectangle(Point(4.5, 6), Point(6, 5))
    mess3 = Text(Point(5.3, 5.5), "Encode")
    mess4 = Text(Point(5, 5), "Resulting Message")
    close_text = Text(Point(5, 1), 'Click Anywhere to Close Window')
    input1 = Entry(Point(6, 8), 25)
    input1.draw(win)
    input2 = Entry(Point(5.1, 7), 15)
    input2.draw(win)
    button.draw(win)
    mess3.draw(win)
    win.getMouse()
    mess3.undraw()
    button.undraw()
    mess4.draw(win)
    secret_message = text_input(input1)
    word = text_input(input2)
    answer = code(secret_message, word)
    encoded = Text(Point(5, 4), answer)
    encoded.draw(win)
    close_text.draw(win)
    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
