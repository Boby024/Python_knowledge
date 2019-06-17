
import sys

def big_Second_Number(my_array):
  my_array.sort(reverse=True)
  lst=my_array
  lst_final=list()
  lst_final.append(lst[0])
  lst_final.append(lst[1])
  return lst_final



my_liste=[]
count=0
average=0
summe = 0
print("enter your number")
for i in sys.stdin:
  (my_liste.append(i))

 # count+=1

#average=summe/count
#print("resultat ", summe)
#sys.stdout.writelines(summe)
print(my_liste)

"""count=int(input("how many values do you have ?"))
inputs = []
average=0
for i in range(count):  # loop 3 times
	inputs.append(input())


for ft in inputs:
    average += float(inputs[ft])
dn=average/len(inputs)
print(dn)


"""
