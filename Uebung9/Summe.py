

def eingabe():
    zahl= int(input("Now start the Summe-program ++ please enter an integer ") )
    if( zahl == 0 ):
        return  zahl
    else:
        return zahl + eingabe()




if __name__ == '__main__':
    print("the summe is : ", eingabe())


