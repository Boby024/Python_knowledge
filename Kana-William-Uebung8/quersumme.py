
def quersum(zahl):
    #zahl = input("For Quersumme-calcul, Please your number! ")
    transf = str(zahl)

    count = 0

    for each_Number in transf:
        count += int(each_Number)

    return count



if __name__ == '__main__':
    print(quersum(222) )

"""

zahl= input("Please your number! ")
transf= str(zahl)

count=0
for each_Number in transf:
    count +=int(each_Number)
print("Quersumme ist : ", count)

"""
