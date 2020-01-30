from quersumme import quersum
from primfaktorzerlegung import primfaktorzerleg


def isNum(a):
    for i in range(len(a)):
        if a[i].isdigit() != True:
            return False

    return True


def eingaben():
    enter=input("Please your number! ")

    if  (isNum(enter)== True):
        #print("good")
        print( "Quersumme is : ",quersum(enter) )
        print("Primfaktorzerlegung is : ", primfaktorzerleg(enter) )

    elif( enter =="Ende" ):
        print("fertig")
    else:
        print("Your input was  wrong, try again to enter an Integer")
        eingaben()



if __name__ == '__main__':
    eingaben()
