phrase = input("Entrer une phrase : ").lower()
compteur = 0
lettre = input("Entrer la lettre à dénombrer : ").lower()
for k in range(len(phrase)):
    if phrase[k] == lettre:
        compteur+=1
print("La phrase saisie comporte, ",compteur,"fois la lettre", lettre)

        

phrase = input("Entrer une phrase : ").lower()
compteur = 0
lettre = input("Entrer la lettre à dénombrer : ").lower()
for car in phrase:
    if car == lettre:
        compteur+=1
print("La phrase saisie comporte, ",compteur,"fois la lettre", lettre)
