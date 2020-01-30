

f = open("Ausgabe.py", "r")

try:
    contain=f.read()
    print(contain)
    f.close()
except FileNotFoundError:
    print("The file was not found")


