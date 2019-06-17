

zahl_1= int(input("enter the first number"))
zahl_2= int(input("enter the second number"))

if ( (zahl_1 % zahl_2==0) or (zahl_2 % zahl_1==0) ):
    print(True)
else:
    print(False)