def caeser(letter, k):

        c = ord(letter) + (k % 26)
        return chr(c);

enter= "MRVPURAXRGGR"
#enter= "JRAA QH QNF UVRE YVRFG, JVEFG QH FRURA, QNFF QVRFR MRVPURAXRGGR XRVARA GVRSRERA FVAA UNG"

txt=""
key=13
final_Liste=[]
for i in enter.split():
    #print( i)
    for j in i:
        transf= caeser(j, key)
        txt+= transf
print(txt)


#print(final_Liste)

#print( "res", ord())
