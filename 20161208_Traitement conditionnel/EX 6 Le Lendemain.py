moisDe30jours=["avril","juin","septembre","novembre"]
moisDe31jours=["janvier","mars","mai","juillet","août","octobre","décembre"]
moisAnnée=["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]

def bissextile(a):
    if a%400==0 or (a%4==0 and a%100!=0):
        test = "année bissextile"
    else:
        test = "année non-bissextile"
    return test

jour = int(input("Saisir le jour d'une date: "))
mois = input("saisir un mois en lettres: ")
année = int(input("Saisir une année: "))

if moisAnnée.index(mois)!=11:
    moisSuivant=moisAnnée[moisAnnée.index(mois)+1]
else:
    moisSuivant=moisAnnée[0]


if mois in moisDe30jours:
    nbrj=30
elif mois in moisDe31jours:
    nbrj=31
elif bissextile(année)=="année bissextile":
    nbrj=29
else:
    nbrj=28

if jour<nbrj:
    print("le lendemain de la date saisie est le",jour + 1,"",mois,"",année)
elif moisSuivant=="janvier":
    print("le lendemain de la date saisie est le 1",moisSuivant,année + 1)
else:
    print("le lendemain de la date saisie est le 1",moisSuivant,année)

