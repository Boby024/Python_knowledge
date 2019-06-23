def toInteger(liste_string):
    one = [liste_string.replace('[', '') for s in x]
    two = [liste_string.replace(']', '') for s in one]
    final = [int(i) for i in two]
    return final

def give_List( liste):
    liste_1= toInteger(liste)
    del liste_1[len(liste_1)-1]
    return liste_1

def give_Integer(liste):
    liste_1= toInteger(liste)
    return liste_1[-1]

def multiplication(ls, integer):
    res=[]
    mul=1
    for i in toInteger(ls):
        mul= i* integer
        res.append(mul)
    return res

def Mul(enter):
    return multiplication( give_Integer(enter) , give_Integer(enter))

x= input("Enter only integer, else you become nothing from this programm ").split(',')


print("the multiplication of this array ",give_List(x), " and of this integer ",give_Integer(x), " is: " ,Mul(x))


#if __name__ == '__main__':
 #   print( multiplication( [32,3,4,8,9,45,62,2] , 2) )

