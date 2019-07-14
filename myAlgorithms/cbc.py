
def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal

def add_XOR(plaintext_number, initial_vector): # only with decimal number
    return plaintext_number ^ initial_vector; # resultat decimal

def caeser( plain_to_Encrypt, key ): # we work here with decimal number
    return plain_to_Encrypt + (key % 26)

# now only plaintext
plaintext= "Welche Eigenschaften sollte ein Pseudo Random Bit Generator erfüllen?"
txt_binary=' '.join(format(ord(x), 'b') for x in plaintext)
# now must a letter
iv="a"
# now must a number
key= 6
#iv_ascii= ' '.join(format(ord(x), 'b') for x in iv) # ord(iv)
liste_txt=txt_binary.split(' ')
liste_resultat=[]
liste_2=[]

for i in liste_txt:
    first_cal = add_XOR(binaryToDecimal(int(i)), ord(iv))
    second_cal = caeser(first_cal, key)
    liste_resultat.append( second_cal )
    liste_2.append(bin(second_cal))


print( liste_resultat)
print( liste_2)

st= 'dhoo'
print( st.strip('dh'))

