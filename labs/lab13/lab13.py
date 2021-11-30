"""
Name: <Jessica Andrews>
<Lab13>.py
Certification of authenticity: I coordinated with Lesly
"""
from graphics import Rectangle, Point
from algorithms import is_in_binary, selection_sort, calc_area
def trade_alert(filename):
    open_file = open(filename, 'r')
    read = open_file.read()
    numbers = read.split()
    for number in range(len(numbers)):
        ints = eval(numbers[number])
        if(ints > 830):
            print("Woe too much! The trade was above 830 at ", number+ 1 ,"seconds")
        elif(ints == 500):
            print("Pay attention dude! Too low! The trade was at 500 at ", number + 1 ,"seconds ")
def main():
    # trade_alert("trades.txt")
    # add other function calls here
    Rect = Rectangle(Point(10,20),Point(20,40))
    list = [10,1,4,6,91,5]
    print(is_in_binary(7,list))
    selection_sort(list)
    print(calc_area(Rect))
    pass


main()
