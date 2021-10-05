"""
Name: <Jessica Andrews>
<Lab6>.py

problem: Problems in lab 6
Certification of authenticity: I coordinated with Lesly
"""


def name_reverse():

    name = str(input('What is your first and last name?'))
    reverse = name.split()
    print(reverse[1]+","+reverse[0])


# name_reverse()

def company_name():

    comp = str(input('What is the internet domain?'))
    name = comp.split(".")
    print(name[1])

# company_name()

def initials():

    students = eval(input("How many students are in your class?"))
    for i in range (0, students):
        first = str(input("What is the first name of student "+str(i+1)))
        last = str(input("What is"+" " + first+"'s"+' last name:'))
        f = first[0]
        l = last[0]
        print(first+"'s"+' initials are '+f+l)


# initials()

def names():

    names = str(input("enter people's names separated by commas:"))
    temp = 0
    indiv_name = names.split(",")
    print("The initials are:", end=' ')
    for i in range (len(indiv_name)):
        indiv_name = names.split(" ")
        f = indiv_name[temp]
        temp+=1
        l = indiv_name[temp]
        temp+=1
        print(f[0]+l[0],end=' ')


# names()

def thirds():

    temp = 0
    how_many= eval(input("how many sentences will you type?"))
    for i in range(how_many):
        phrase = str(input("please write your phrases"))
        for n in range(0,len(phrase)-1,3):
            print(phrase[n])


# thirds()

def word_average():
    aver = 0
    count = 0
    loop_it = eval(input("how many sentences will you type?"))
    for i in range(loop_it):
        phrase = str(input("what will your phrase be?"))
        words = phrase.split(' ')
        for n in range(len(words)):
            count = count + len(words[n])
            aver = count/len(words)
    print(aver)
word_average()
