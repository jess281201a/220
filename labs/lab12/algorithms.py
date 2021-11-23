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







