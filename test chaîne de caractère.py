phrase1 = 'Bonjour ! '
phrase2 = "Tout le monde !! "
phrase = phrase1 + phrase2
print (phrase)



phrase1 = input("Entrer un phrase : ").lower()
phrase2 = input("Entrer une autre phrase : ").upper()
phrase = phrase1 + phrase2
print (phrase)



phrase1 = input("Entrer un phrase : ").upper()
phrase2 = input("Entrer une autre phrase : ").upper()
voyelles , speciaux = "AEIOUY" , " !"
phrase = phrase1 + phrase2
print (phrase, "a une longueur de ",len(phrase))
for k in range(len(phrase)):
    if phrase[k] in voyelles:
        print(phrase[k], "est une voyelle")
    elif phrase[k] not in speciaux:
        print(phrase[k]," est une consonne .")
   


phrase1 = input("Entrer un phrase : ").upper()
phrase2 = input("Entrer une autre phrase : ").upper()
voyelles , speciaux = "AEIOUY" , " !"
phrase = phrase1 + phrase2
print (phrase, "a une longueur de ",len(phrase))
for car in phrase:
    if car in voyelles:
        print(car, "est une voyelle")
    elif car not in speciaux:
        print(car," est une consonne .")
