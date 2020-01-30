
zahl=int(input("enter your number: "))
list_Array= list()
i=0
while(zahl> i):
    list_Array.append(zahl)
    zahl=int(input("enter your number: "))
print(list_Array)


count=0;
together=0;
just=list_Array
for checker in list_Array:
    for number in list_Array:
        if(checker== number):
            count+=1
            together=(count,checker)
   # print( "for: ",checker, "appear: ", count)
    count=0
    #just.append(together)
   # print(together)
#nim=int(input("which number would you know the number of apparition on the programm"))




"""
for fr,g in enumerate (list_Array):
    print(fr,g)
    
j=0
k=0
count=0;
while(len(list_Array) > 0):
    if( list_Array[j] ==list_Array[k]):
        count+=1
        print(count)
        k+=1;
    j+=1
"""


"""
j=0;
k=0;
second_Array=list()
for first in list_Array:
    for second in list_Array:
        if(first== second ):
            j+=1
            second_Array.append(first)


print(second_Array)
print(j)

#print(list_Array)

"""