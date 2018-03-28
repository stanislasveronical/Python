n=int(input("Entrer la valeur de n : "))
compteur=0

Tab = [i for i in range (n+1)]
for i in range(1,n+1):
    if not i%10:
        print(Tab[i])
    else:
        print(Tab[i],'\t',end = " ")
print("\n")
for i in range(2,n+1):
    for j in range(i+1,n+1):
        if not j%i:
            Tab[j]=0
print("Liste des entiers naturels premiers inférieurs ou égaux à ",n)
for i in range(2,n+1):
    if Tab[i]:
        compteur=compteur+1

        print(Tab[i],'\t',end=" ")
print("\n")
print("Il y a ",compteur,"nombres premiers jusqu'à ", n)
print("Soit une proportion de",proportion)

