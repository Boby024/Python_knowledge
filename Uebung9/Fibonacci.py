
def fib(number):

    if (number <= 1 ):
        return number
    else:
        return  fib(number - 1) + fib(number-2)


if __name__ == '__main__':
    zahl = int(input("please enter an integer for Fibonacci calcul "))
    print(fib(zahl))

