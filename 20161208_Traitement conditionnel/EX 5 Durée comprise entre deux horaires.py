h1 = 60 *int(input("entrer l'heure du début :"))
m1 = int (input("Entrer les minutes de début :"))
h2 = 60*int(input("Entrer l'heure de fin :"))
m2 = int (input("Entrer les minutes de fin :"))
durée = (h2+m2)-(h1+m1)
h = durée//60
m = durée%60
print ("La durée entre les deux horaires est de :", h,"heures et",m, "minutes")
