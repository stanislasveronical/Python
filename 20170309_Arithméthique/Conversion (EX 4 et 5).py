#Conversion en hexadecimal

dec = int(input("Saisir l'écriture decimal d'un entier naturel n : "))
hex = []
liste_chiffres = "ABCDEF"
q = dec
while q!=0:
    hex = [q%16] + hex
    q = q//16
print("L'écriture de ",dec,"dans le systeme hexadecimal est ",end="")
for i in range(len(hex)):
    if hex[i]>=10:
        print(liste_chiffres[hex[i]%10],end="")
    else:
        print(hex[i],end="")
print("\n")
    

#Conversion inverse
liste_chiffres = "ABCDEF"
hexa = input("Saisir l'écriture hexadecimale d'un entier naturel n : ")
l , n = len(hexa) , 0
for i in range(l):
    if hexa[i] in liste_chiffres:
        n = n + (ord(hexa[i])-55)*16**(l-1-i)
    else:
        p = int(hexa[i])
        n = n + p*16**(l-1-i)
print("L'entier ayant pour ecriture hexadecimale ",hexa,"est : ",n)
