def product(liste):
    try:
        # with this Line we are able to put all input into an Array
        res = 1
        for i in liste:
            res *= float(i)
        return res
       # print("the product of ", x, " ist ", res)
    except ValueError:
        #print(" Error become you entered string and there are your number", x)
        return "Error because you entered string in your array"

def multiplication(array, integer):
    try:
        # with this Line we are able to put all input into an Array
        res = []
        mul = 1
        for i in array:
            mul = float(i) * integer
            res.append(mul)
        return res
    except ValueError:
        return "Error because you entered string in your array or the value of your integer is wrong "

def verdoppeln( array):
    try:
        res = []
        mul = 1
        for i in array:
            mul = float(i) * (-1)
            res.append(mul)
        return res

    except ValueError:
        return "Error because you entered string in your array "

enter = input("Enter only integer, else you become nothing from this programm ").split()

# the original array list from the user
copie_enter=[]
for i in enter:
    copie_enter.append(i)

# here the last character form the array is extracted and then delete from the array
last= enter[-1]
enter.remove(last)

if (last == 'p'):
    print("Your original array list is ", copie_enter )
    print( "your product ist ",product(enter) )
elif (last == 'm'):
    print("your multiplication is ", multiplication(enter, int(input("your integer "))))
    print("Your original array list is ", copie_enter)
elif (last == 'd'):
    print("Your original array list is ", copie_enter)
    print("your verdoppeln-programm ",verdoppeln(enter))

#x = [int(i) for i in input("enter input values ").split()]  32 3 4 8 9 45 62 2   32.1 3.2 4.5 8.7 9.2 45.9 62.3 2.1
