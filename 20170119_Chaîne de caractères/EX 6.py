phrase = input("Entrer un phrase à tester : ").lower()
alphabet = "abcdefghijklmnopqrstupwxyz"
compteur = 0
for lettre in alphabet:
    if lettre in phrase:
        compteur+=1
if compteur == 26:
    print("La phrase",phrase,"est un pangramme car elle comporte au moins une fois les 26 lettres de l'alphabet")
else:
    print("La phrase", phrase,"n'est pas un pangramme car elle comporte seulement",compteur," lettres parmi les 26 lettres de l'alphabet")
    
