def verified_enter(word):
    lis_words = ["ja", "nein"]
    if (word not in lis_words):
        return "not good"
    else:
        return "good"


def loop():
    enter = input("enter ja or nein ")
    if( verified_enter(enter)== "not good"):
        return "TRY AGAIN your input don't exist in our database, you have to choice between ja and nein"
        loop()
    elif(verified_enter(enter)== "good"):
        if (str(enter) == "nein"):
            return "sauber"
        elif (str(enter) == "ja"  ):
            loop()
            return "endlich mal"




print( loop() )

#n= input("enter ja or nein ")
#print( verified_enter(n))
