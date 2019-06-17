
def Isprim(number):
    if(int(number) % 2==0):
        return False
    else:
        return True

def divider_Test(number):
    stored_dvd =0
    for dvd in range(2, int(number+1) ):
        if( number % dvd ==0):
            stored_dvd=dvd
            break

    return stored_dvd

#zahl= int(input("Please enter your number for Primfaktorzerlegung except numbers like 2 and 3! "))

def primfaktorzerleg(zahl_1):
    zahl=int(zahl_1)
    store_nbr = []

    if (Isprim(zahl) == False and zahl > 2 and zahl > 3):
        while (zahl > 1):

            divider = divider_Test(zahl)
            if ((zahl % divider) == 0):
                store_nbr.append(divider)
                zahl = zahl / divider
        #print("Primfaktorzerlegung for your number is: ", store_nbr)
        return store_nbr
    else:
        #print("your number is a prime number or is smaller than 3 :) ")
        return "your number is a prime number or is smaller than 3 :) "


if __name__ == '__main__':
   print( primfaktorzerleg(16))

"""
zahl= int(input("Please enter your number for Primfaktorzerlegung except numbers like 2 and 3! "))

store_nbr=[]
divider_store=0
divider=0
if(Isprim(zahl) == False and zahl > 2 and zahl>3 ):
    while( zahl > 1 ):
        # zahl_plus= zahl + 1
         #      for store_divider in range(2, int(zahl_plus) ):
          #  divider= store_divider 
        divider= divider_Test(zahl)
        if ( (zahl % divider) == 0):
            store_nbr.append(divider)
            zahl = zahl / divider
    print("Primfaktorzerlegung for your number is: ",store_nbr)
else:
    print("your number is a prime number or is smaller than 3 :) ")
"""
