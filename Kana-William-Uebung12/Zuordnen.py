

with open("Herrchen.txt","r") as lies :
    save_Herrchen= lies.readlines()
    ord_List_1= sorted(save_Herrchen)

with open("Hunde.txt","r") as lies :
    save_Hunde= lies.readlines()
    ord_List_2 = sorted(save_Hunde)

ls=[]
liste= {}
for i in ord_List_1:
    for j in ord_List_2:
        if( i[0] == j[0] ):
            #geordnete= (i,j)
            #ls.append(geordnete)
            liste.update( {i:j} )

#lire.close()

for k, v in liste.items():
    with open("geordnet.txt", "a") as lire:
        lire.write("Inhaber {} : HundeName {} ".format(k,v) )
        lire.writelines("\n")
print( liste )
