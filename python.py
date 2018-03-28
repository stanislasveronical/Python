from random import*
n=randrange(1,100)
devine = int(input("Deviner le nombre choisi : "))
tentatives=int

while tentatives<10:
    if (devine == n):
        print("Felicitation")
        if devine < n:
            print("Le nombre choisi est plus petit")
        else:
            print("Le nombre choisi est plus grand")



