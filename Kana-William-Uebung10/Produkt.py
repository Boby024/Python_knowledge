def product(liste):
    try:
        # with this Line we are able to put all input into an Array

        res = 1
        for i in liste:
            res *= int(i)
        print("the product of ", x, " ist ", res)
    except ValueError:
        print(" Error become you entered string and there are your number", x)


x = input("Enter only integer, else you become nothing from this programm ").split()
product(x)

#x = [int(i) for i in input("enter input values ").split()]
