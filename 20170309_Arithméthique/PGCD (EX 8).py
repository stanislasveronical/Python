a=int(input("Entrer un nombre a : "))
b=int(input("Entrer un nombre b : "))
a1 , b1 = a , b

while a1%b1:
    a1 , b1 = b1 , a1%b1
print("Le PGCD de ",a," et de",b," vaut : ", b1)
