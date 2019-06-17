import random


def cal_Gain(price, zahl):
    # if( pr==True):

    gain = 0;
    choice_Number = random.randrange(0, 50)

    if (zahl == choice_Number):
        gain = price + (3 * price)
        # print("You win ", gain, "$")
        # print(" The choiced number was : ", choice_Number)
        return gain
    elif (zahl % 2 == 0 and choice_Number % 2 == 0):
        gain = price + (price / 2)
        # print("You Win  ", gain, "$")
        # print(" The choiced number was : ", choice_Number)
        return gain
    elif (zahl % 2 != 0 and choice_Number % 2 != 0):
        # print("You Win  ", gain, "$")
        return gain
    else:
        return "Es tut uns leid => keine Chance gehabt, Aber Sie können noch versuchen because the number was ", choice_Number
        # print(" because the choiced number was : ", choice_Number)


resultat=0
#res=bool
#somme_mise=0
#nbr=0
somme_mise = (input("How much  would you like to bet ? "))
nbr = (input("Please enter your number : "))
while(True):

    if( isinstance(somme_mise or nbr ,str)  ): #or isinstance(nbr,str)
        #resultat=cal_Gain(somme_mise,nbr)
        #print("input is wrong")
        somme_mise = (input("How much  would you like to bet ? "))
        nbr = input("Please enter your number : ")

    else:

        resultat = cal_Gain(somme_mise, nbr)

print(resultat)


"""
res= bool
try:

    somme_mise = int(input("How much  would you like to bet ? "))
    nbr = int(input("Please enter your number : "))
    res=True
except ValueError:
    res=False
    #print("Please enter only number ")
"""
