import sys

def vokal_count(vokal):
    list_vokabel = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    if (vokal in list_vokabel):
        return True
    else:
        return False

def anfangsbuchstabe(string_word):
    if( ord(string_word) > 64 and ord( string_word )< 91  ):
        return True
    else:
        return False

first_List = []
summe = 0
for el in sys.stdin:
	first_List += [el]
#print(first_List)

second_List=[]
for eachLine in first_List:
     second_List.append(eachLine.split())

final_List=[]
for each_String in second_List:
    for each_String_2 in each_String:
        final_List.append(each_String_2)
#print(final_List)

# each strings are separeted in character
give_count=0
resultat_count=0
for string_List in final_List:
    for character in string_List:
        #print(character)
        if(vokal_count(character) == True):
            give_count += 1
#resultat_count += give_count
print("Vokale : ",give_count)

count=0
for start_string in final_List:
    if( anfangsbuchstabe(start_string[0]) ==True  ):
        count +=1
print("Anfangsbuchstabe groß : ",count)



