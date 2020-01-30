
list_Array=list()
for erste in range(1,31 ):
    if(erste%3 ==0):
        list_Array.append(erste)

list_Array.sort( reverse = True )

for first in list_Array:
    print(first)



""""

brandsList =["Dell", "HP", "Lenovo", "Acer", "Asus", "Apple", "Samsung", "MSI", "Alienware", "Razer", "Huawai", "LG",
             "Hyundai", "Latitude","PANASONIC", "XPS", "jumper", "Notebook flexx", "Proscan","Google","Microsoft"]
brandsList.sort(reverse = False)
print( brandsList )

"""
