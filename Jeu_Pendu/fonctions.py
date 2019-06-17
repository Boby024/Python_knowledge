import random

def prend_word(name):
    lst=["manger"]
    choiseW= random.choice(lst)
    auf= list(choiseW)

    enter= input()
    position=0

    for i,w in enumerate(auf):
        if w== enter:
            position=i
        print("other word ")
    else:
        position=i

    print(" find nothing ")

gleanTrue
