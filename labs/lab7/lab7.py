"""
Name: <Jessica Andrews>
Partner: <Lesly>
<Lab7>.py
"""
from math import pi

def cash_conversion():
    amount = eval(input("What integer will you give me?"))
    print("$"+'{:.2f}'.format(amount))

def encode():
    message = str(input('What is your secret message?'))
    num = eval(input('What is your key value?'))
    cipher = ""
    for i in message:
        conv = ord(i)+ num
        letter_conv = chr(conv)
        cipher = cipher + letter_conv
    print(cipher)

def sphere_area(radius):
    area = 4 * pi * radius ** 2
    return area


def sphere_volume(radius):
    volume = (4/3) * pi * radius ** 3
    return volume

def sum_n(n):
    temp = n
    for i in range(n):
        temp =+ temp + i
    return temp

def sum_n_cubes(n):
    temp = n
    add = 0
    for i in range(n):
        cube = pow(i+1,3)
        add = add +cube
    return add

def encode_better():
    message = str(input('What is your secret message?'))
    key = str(input('What is your key?'))
    cipher = ""
    for i in range(len(message)):
        conv = ord(key[i]) - 97
        l_conv = ord(message[i]) + conv
        letter_conv = chr(l_conv)
        cipher = cipher + letter_conv
    print(cipher)

def main():
     #add function calls here
     pass
     cash_conversion()
     encode()
     sphere_area()
     sphere_volume()
     sum_n()
     sum_n_cubes()
     encode_better()
main()
