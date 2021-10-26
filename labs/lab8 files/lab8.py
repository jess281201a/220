"""
Name: <Jessica Andrews>
Partner: <Lesly>
<Lab8>.py
"""
# Add your encryption methods here
from encryption import encode, encode_better

def number_words(in_file_name,out_file_name):
    open_walrus = open(in_file_name,'r')
    output = open(out_file_name, 'w')
    body = open_walrus.read()
    word = body.split()
    print(word)
    for line in range(len(word)):
        message = (str(line+1) + " " + word[line] +"\n")
        output.write(message)

def hourly_wages(in_file_name, out_file_name):
    open_hourly = open(in_file_name,'r')
    open_output = open(out_file_name,'w')
    body = open_hourly.read()
    info = body.split("\n")
    for line in range(len(info)):
        separate_list = info[line].split()
        print(len(separate_list))
        print(separate_list)
        mult = eval(separate_list[2])+1.65
        open_output.write(separate_list[0]+" "+separate_list[1] + " " + str(mult)+"\n")

def calc_check_sum(isbn):
    numbers = isbn.replace('',' ')
    number = numbers.split(" ")
    times = 10
    count = 0
    for i in range (1,len(number)-1):
        num = eval(number[i]) * times
        count = count + num
        times = times -1
    return(count)

def send_message(file, friend):
    open_file = open(file, 'r')
    friend_open = open(friend,'w')
    message = open_file.read()
    friend_open.write(message)

def send_safe_message(file, friend,key):

    open_file = open(file, 'r')
    friend_open = open(friend,'w')
    message = open_file.read()
    friend_open.write(encode(message,key))

def send_uncrackable_message(file, friend):

    open_file = open(file, 'r')
    friend_open = open(friend,'w')
    message = open_file.read()
    friend_open.write(encode(encode_better(file)))


def main():
    # calc_check_sum('0072946520')
    # number_words("Walrus.txt","output.txt")
    # hourly_wages("hourly_wages.txt","new_wage.txt")
    # send_message('message.txt','Jessica')
    # send_safe_message("secret_message.txt","Jason",5)
    send_uncrackable_message("pad.txt","Timo")
    pass
main()