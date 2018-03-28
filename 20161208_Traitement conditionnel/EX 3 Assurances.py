Montant = float(input('Saisissez Le montant des dommages :'))
Franchise = (Montant*0.9)

if (Franchise <= 15) and (Franchise >= 50):
    print ('Le montant', Montant, "est à la charge de l'assuré")
else :
    print ('Le montant', Franchise, "est à la charge de l'assuré")
#Fin Si
