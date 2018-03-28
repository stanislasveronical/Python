C = float(input("Saisissez votre Capital Initial : "))
n = int(input("Saisissez le nombre d'année : "))
i = float(input("Saisissez le taux d'interets : "))

for k in range (1,n+1):
    C=C*(1+i)
print("Vous disposez à présent de",C,"euros")














C = float(input("Saisissez votre Capital Initial : "))
n = int(input("Saisissez le nombre d'année : "))
i = float(input("Saisissez le taux d'interets : "))
d =2*C

for k in range (1,n+1):
    C = C * (1+i)
    if C>=d:
        print("Capital doublé en ",k,"années")
        print("Il vaut alors" ,C,"euros")
        break





