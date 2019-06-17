import sys

def extractNumber(phrase):
    final_List = []
    second_List = []
    no_float_List = []
    for array_Element in phrase:
        second_List = array_Element.split()
        for togo in second_List:
            try:
                float(togo) or int(togo)
                final_List.append(togo)
            except ValueError:
                no_float_List.append(togo)
    return final_List




your=sys.argv[1]
trans=str(your)
storeZahl=[]
try:
    with open(trans, "r") as enterFile:
        storeZahl = enterFile.readlines()
    transform = extractNumber(storeZahl)
    print(transform)
except FileNotFoundError:
    print("the name of file is not correct")




