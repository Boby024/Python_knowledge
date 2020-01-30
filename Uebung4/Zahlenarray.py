

myArray=list()
i=0
count=int(input("how much number will you enter for this test: "))
#zahl=int(input("now enter your number: "))
while( (count) > i):
    zahl=int(input("now enter your number: "))
    myArray.append(float(zahl))
    i+=1
print(myArray)

origin=list()
for first in myArray :
    origin.append(first)


myArray.sort(reverse = True )
biggest=myArray[0]
smallest=myArray[len(myArray)-1]
new_Array=list()
new_Array.append(smallest)
new_Array.append(biggest)

#print("the biggest number is: ",biggest)
#print("the smallest number is: ",smallest)

print("old array: ", origin)
print("new array:" ,new_Array)

