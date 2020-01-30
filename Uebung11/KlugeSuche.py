
def suche(liste,a):
    try:
        return liste.index(a)
    except ValueError:
        return -1

def sucheIndex(liste, a):
    for i in range(a, len(liste)):
        if(liste[i] ==a ):
            return i
    return -1

# Komplexitätsklasse: stabil

if __name__ == '__main__':
    my_liste = [2, 9, 5, 6, 1, 0]
    zahl=1
    print("The element exists in the Liste and the index is: ", sucheIndex(my_liste,1 ) ,"\n")
    print("The element don't exist in the Liste : ", sucheIndex(my_liste, 3), "\n")

    if( sucheIndex(my_liste, zahl)== -1 ):
        print("resultat: ", -1)
    else:
        print( "resultat: ", sucheIndex(my_liste,zahl))
