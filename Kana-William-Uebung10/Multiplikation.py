def toInteger(liste_string):
    final = [int(i) for i in liste_string]
    return final

def multiplication(ls, integer):
    res=[]
    mul=1
    for i in toInteger(ls):
        mul= i* integer
        res.append(mul)
    return res

# here there is still error to revise
def move_Ganzzahl(liste_Integer):
    nbr= len(liste_Integer) -1
    return list[nbr]

x= input("Enter only integer, else you become nothing from this programm ").split(',')
one=[s.replace('[', '') for s in x]
two=[s.replace(']', '') for s in one]
#print(two)
liste= toInteger(two)
zahl= liste[-1] #move_Ganzzahl( liste )
del liste[len(liste)-1]
print(liste)
print("the multiplication of this array ",liste, " and of this integer ",zahl, " is: " ,multiplication( liste,zahl))

#if __name__ == '__main__':
 #   print( multiplication( [32,3,4,8,9,45,62,2] , 2) )

