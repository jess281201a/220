"""
Name: <Jessica Andrews>
<Lab10>.py

problem: Problems in lab 9
Certification of authenticity: I coordinated with Lesly
"""
def create_board():
    board_nums = ["1","2","3","4","5","6","7","8","9"]
    return board_nums

def draw_board(list):
    draw = list
    print(draw[0] + "|"+draw[1] + "|" + draw[2])
    print("______")
    print( draw[3] + "|" + draw[4] + "|" + draw[5])
    print("______")
    print(draw[6] + "|" + draw[7] + "|" + draw[8])

def change(board,position,character):
    character = character.upper()
    if character == "X" or character == "O":
        board[position-1] = character
        draw_board(board)
    else:
        print("Nah fam that's invalid >:(")

def validate(var):
    change = str(var).isnumeric()
     # print(change) # false
    if change:
        return True
    else:
        return False

def win(board):
    if board[0] == board [1] == board[2]:
        return True
    elif board[3] == board[4] == board[5]:
        return True
    elif board[6] == board [7] == board[8]:
        return True
    elif board[0] == board [3] == board[6]:
        return True
    elif board[1] == board [4] == board[7]:
        return True
    elif board[2] == board [5] == board[8]:
        return True
    elif board[0] == board [4] == board[8]:
        return True
    elif board[2] == board [4] == board[6]:
        return True
    else:
        return False

def main():
    print("Hello! Please print your position you chose first and if you will be using X or O capitalization does not matter!")
    create = create_board()
    draw_board(create)
    for i in range(len(create)):
        if win(create) == False:
            command = input("Please enter a position and character")
            new = command.split(" ")
            number = int(new[0])
            if validate(create[number - 1]) == True:
                change(create,number,new[1])
            else:
                print("Not Valid!")
        else:
            print("player " + new[1] + " wins!")
            break
    pass

main()
