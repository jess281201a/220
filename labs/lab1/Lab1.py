"""
Name: <Jessica Andrews>
lab1.py

Problem: This function calculates the area of a rectangle
"""
def calc_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)
calc_area()

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = width * length * height
    print("The volume is:",volume)
calc_volume()

def shooting_percentage():
    totalShots = eval(input("How many shots in total?:"))
    shotsMade = eval(input("how many did you make?:"))
    percentage = shotsMade / totalShots *100
    print("Your shooting percentage is:",percentage)
shooting_percentage()

def coffee():
    pounds = eval(input("How many pounds of coffee are you buying?"))
    coffeeCost = 10.50
    shippingCost = 0.86 * pounds
    fixed = 1.50
    total = coffeeCost + shippingCost +fixed
    print("the total cost is:",total)
coffee()

def kilometers_to_miles():
    kilometers = eval(input("how many kilometers did you drive?:"))
    converstion = kilometers/1.61
    print("you drove:",converstion,"miles")
kilometers_to_miles()

 #this quotes is to add an amendment