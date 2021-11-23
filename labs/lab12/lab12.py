"""
Name: <Jessica Andrews>
<Lab12>.py
Problem : lab 12 problems
Certification of authenticity: I coordinated with Lesly
"""
from algorithms import read_data, is_in_linear
from random import randint

def find_and_remove_first(list,value):
    find = list.index(value)
    list.remove(value)
    list.insert(find,"Jess")
    print(list)

def good_input():
    user_input = eval(input("What is your number"))
    while user_input < 0 or user_input >10:
        if user_input > 10:
            user_input = eval(input("Number is way to high! Lower it!"))
        elif user_input < 0:
            user_input = eval(input("Number is too low we need a higher one"))
    return user_input

def num_digits():
    temp = 1
    user_input = eval(input("What number are you picking"))
    while user_input >= 0:
        if user_input != 0:
            numbers = user_input//10
            temp += 1
            print(temp)
        user_input = eval(input("What number are you picking"))
    else:
        temp = 1
        print(temp)
    if user_input <= 0:
        return
    return temp

def hi_lo_game():
    temp = 0
    right_num = randint(0, 100)
    user_input = eval(input("What is your guess?"))
    while temp != 7:



def main():
    find_list = [5,7,4,8,4,12,4,8]
    find_and_remove_first(find_list,8)
    list = read_data("read_data_test_data.txt")
    is_in_linear(13,list)
    # good_input()
    num_digits()

    pass


main()
