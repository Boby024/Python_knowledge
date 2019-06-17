first_List=['Wekjnkwwoe Aoij owieg oiwe fowe owigj oiwgw\n', 'gwgowi gj anl\n', 'an,dynvv wgowiew  oiwjf oiajnk\n', 'anv,xcvmwwi hfwioh oeoew\n']
#second_List_1= [['wekjnkwwoe', 'woij', 'owieg', 'oiwe', 'fowe', 'owigj', 'oiwgw'], ['gwgowi', 'gj', 'anl'], ['an,dynvv', 'wgowiew', 'oiwjf', 'oiajnk'], ['anv,xcvmwwi', 'hfwioh', 'oeoew']]

#count_Strings= len(lis)
#print(count_Strings)
#print(lis[1])

second_List=[]
for eachLine in first_List:
     second_List.append(eachLine.split())

#print(second_List)

#print(second_List_1[0])
#print(second_List_1[1])
final_List=[]
for each_String in second_List:
    for each_String_2 in each_String:
        final_List.append(each_String_2)
print(final_List)

for ea in final_List:
    for k in ea:
        print(k)

list_vokabel = ['a', 'e', 'i', 'o', 'u']
if ('asdvjksn' in list_vokabel):
    print(True)
else:
    print( False )
g='A'
print( ord(str(g)))

def anfangsbuchstabe(string_word):
    if(  ord(string_word) > 64 and ord( string_word )< 91  ):
        return True
    else:
        return False

count=0
for start_string in final_List:
    if( anfangsbuchstabe(start_string[0]) ==True  ):
        count +=1
print(count)
