from graphics import Rectangle
def read_data(filename):
    i = 0
    open_file = open(filename,"r")
    numbers = open_file.read()
    list = numbers.split()
    new_list = []
    while i < len(list):
        new = eval(list[i])
        new_list.append(new)
        i += 1
    open_file.close()
    return new_list

def is_in_linear(search_value,values):
    i = 0
    try:
        while i < len(values):
            find_index = values.index(search_value)
            if values[find_index] == search_value:
                answer = True
            i += 1
    except:
        answer = False
    return answer

def is_in_binary(search_val,values):
    left = 0
    right = len(values) -1
    while left <= right:
        middle = (left+right)//2
        middle_value = values[middle]
        print(middle_value)
        if search_val == middle_value:
            return True
        if search_val < middle_value:
            right = middle -1
        if search_val > middle_value:
            left = middle + 1
    return False

def selection_sort(values):
    num = len(values)
    for low in range(num - 1):
        lowest = low
        for i in range(low+1,num):
            if values[i] < values[lowest]:
                lowest = i
        values[low],values[lowest] = values[lowest], values[low]
    print(values)

def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    p1x = p1.getX()
    p2x = p2.getX()
    p1y = p1.getY()
    p2y = p2.getY()
    width = abs(p2x) - abs(p1x)
    hight = abs(p2y) - abs(p1y)
    area = width * hight
    return area


def rect_sort(rectangles):
    area = calc_area(rectangles)
    num = len(area)
    for low in range(num - 1):
        lowest = low
        for i in range(low+1,num):
            if area[i] < area[lowest]:
                lowest = i
        area[low],area[lowest] = area[lowest], area[low]
    print(area)
