

def openFiLe(nameFile):

    try:
        with open(nameFile, "r")as fileOpen:
            each_line= fileOpen.readlines()

            i=len(each_line)
            j=0
            my_List=[]

            # That is my Methode
            #while(i >  0):
             #   my_List.append(each_line[i-1])
                #l=len(each_line)
               # i -=1

            # advice of the corrector
            for i in range(len(each_line) - 1, -1, -1):
                my_List.append(each_line[i])

            new_List= my_List

        with open("new_File.txt", "w") as new_File:
            new_File.writelines(new_List)

        return  new_List

    except FileNotFoundError:
        return "file not exist"


file_Name= "texterFile.txt"
openFiLe( file_Name)
#print( openFiLe( file_Name) )

with open("new_File.txt","r") as read_File:
    begin=read_File.read()
print(begin)

