import sys

zahl_1= sys.argv[1]
zahl_2= sys.argv[2]
zahl_3= sys.argv[3]

#wenn Sie alle gleich sind
if( zahl_1== zahl_2 and zahl_2== zahl_3 ):
    print("Gleich")

elif ( zahl_1== zahl_2 and zahl_2 < zahl_3 ):
    print("Aufsteigend sortiert")

elif ( zahl_1< zahl_2 and zahl_2< zahl_3):
    print("Aufsteigend sortiert")

elif ( zahl_1> zahl_2 and zahl_2> zahl_3) :
    print("Absteigend sortiert")

else:
    print("Unsortiert")
