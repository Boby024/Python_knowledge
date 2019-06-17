from Fibonacci import fib
from Summe import eingabe


try:
    y = int( input("What should you enter between an integer for Fibonacci-calcul or press direct enter-taste for Summe-program ") )
except ValueError:
    y=None

if y is None:
    print( eingabe())
else:
    print("Now Fibonacci-program: the solution of this number ist :",fib(y))
