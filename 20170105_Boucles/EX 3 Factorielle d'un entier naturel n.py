n = int(input("Saisir un entier n : "))
factorielle = 1
i = 1
while i <= n:
    factorielle = factorielle * i
    i = i + 1
print("La factorielle de", n, "vaut", factorielle)
