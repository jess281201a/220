import math
"""
Name: Jessica Andrews
<lab2>.py
Problem: Math calculations done in python
"""

def sum_of_threes():
   number = eval(input("What will be your upper bound number?:"))
   for num in range(3,number,3):
        3**num
        print(num)
    #ended for-loop
sum_of_threes()

def multiplication_table():
    for row in range(1,11):
        for column in range(1,11):
            print(row*column, end="\t")
        print()
multiplication_table()

def traingle_area():
    a = eval(input("what is the length of side A?"))
    b = eval(input("What is the length of side B"))
    c =eval(input("What is the length of side C"))
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The area of the triangle is", area)
traingle_area()

def sumSquares():
   l =  eval(input("what is your lower bound?"))
   u = eval(input("what is your upper bound"))
   for num in range(l,u):
      number = l**2 +num**2 +u**2
   print(number)
sumSquares()

def power():
   p = 1
   b = int(input("What is the base?:"))
   e = int(input("What is the exponent?:"))
   for i in range (1,e+1):
    p=p*b
   print(b,"^",e,p)

power()





