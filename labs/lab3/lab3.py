"""
Name: <Jessica Andrews>
lab.py

Point: Solving the programs in lab 3
Certification of authenticity: I collaborated with Leslie and Katie
"""


def average():

    hw1 = eval(input("Enter your grade on HW1:"))
    hw2 = eval(input("Enter your grade on HW2:"))
    aver = (hw1 + hw2)/2
    print("Your average of these two homework grades is:", aver)


average()


def tip_jar():
    add = 0
    for i in range(0, 5):
        tip = eval(input("What would you like to put in the tip jar?:"))
        add = tip + add
    print("The final amount in the tip jar is:", add)


tip_jar()


def newton():
    var = eval(input("What would you like the variable X to be?:"))
    approx = eval(input("How many time would you like to improve the approximation?:"))
    improve = var / 2
    for i in range(0, approx):
        improve = (improve + var/improve)/2
    print("the approximation of this is:",improve)

newton()


def sequence():
    terms = eval(input("How many numbers will be in your series?:"))
    temp = 1
    for i in range(0,terms):
       remain = i % 2
       temp = temp + 2 * remain
       print(temp)


sequence()

#I dont even know, sorry
def pi():
    temp = 2
    n = eval(input("What would you like N to be?:"))
    for i in range (0, n):
        remain = i % 2
        temp = temp + 2 * remain
        temp1 = 1
        remain1 = i % 2
        temp1 = temp1 + 2 * remain1
        output = remain / remain1
    print("This is the answer:", output)



pi()


