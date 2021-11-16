"""
Name: <Jessica Andrews>
<Lab11>.py
Problem:Create a hang man game
Certification of authenticity: I coordinated with Lesly
"""
from random import randint
def read_file():
    read_file = open("wordlist.txt",'r')
    lists = read_file.readlines()
    read_file.close()
    return lists

def pick_words(words):
    word = str(words[randint(0,len(words)-1)])
    return word

def lets_guess(secret_word,letter,unguessed):
    find_word = secret_word.find(letter)
    word_seperated = list(secret_word)
    find_letter = word_seperated[find_word]
    letters = secret_word[find_word]
    if find_word >= 0:
        unguessed[find_word] = letters
        print(unguessed)
    else:
        count =+ 1
        if count <= 7:
            print("Ooops! One life lost!")
        else:
            print("sorry! Game Over")

def check(list):
    if "_" not in list:
        return True

def play():
    unguessed = []
    lists = read_file()
    word = pick_words(lists)
    read = read_file()
    words = pick_words(read)
    print(word)
    print("Hey! Lets guess some words! Print a letter and lets see if its right!")
    guess = input("What letter will you guess")
    guesses= guess.lower()
    for i in range(len(word) - 1):
        unguessed.append("_")
    print(unguessed)
    while guesses == guesses:
        lets_guess(word,guess,unguessed)
        guess = input("What letter will you guess")
        guesses.lower()
    if check(unguessed) == True:
        print("Yay! You have finished!")





def main():
    play()

    pass


main()
