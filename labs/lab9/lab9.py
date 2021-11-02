"""
Name: <Jessica Andrews>
<Lab9>.py

problem: PRoblems in lab 9
Certification of authenticity: I coordinated with Lesly
"""
def addTens(nums):
    numbers = []
    for i in range (len(nums)):
        new = nums[i] +10
        nums[i]=new
    # return numbers

def squareEach(nums):
    numbers = []
    for i in range(len(nums)):
        new = nums[i] * nums[i]
        nums[i]=new
    # return numbers

def sumList(nums):
    numbers = []
    add = 0
    for i in range(len(nums)):
        add =nums[i] + add
    return add


def toNumbers(strList):
    for i in range(len(strList)):
        string = (strList[i])
        strList[i] = (eval(string))
    # return strList

def writeSumOfSquares():
    input_name = input('What file will you choose? Dont forget to add .txt at the end')
    openFile = open(input_name,'r')
    outFile = open("sum_out.txt",'w')
    body = openFile.readlines()
    for line in body:
        delete = line.strip()
        info = delete.split(" ")
        toNumbers(info)
        squareEach(info)
        answer = sumList(info)
        outFile.write("Sum of squares = "+str(answer)+"\n")
# writeSumOfSquares()


def leapYear(year):
    ans = ""
    if year % 400 == 0 :
        ans = "Is leap year"
    elif not(year % 100 == 0) and year % 4 == 0:
        ans = "Is leap year"
    else:
        ans ="Is not leap year"
    print(year, ans)
leapYear(2012)

"""  
def main():
    list = ["3","6","9"]
    print(list)
    toNumbers(list)
    print(print(list))
main()
"""