from random import*
n = int(input("Entrer le nombre d'éléments à trier : "))
Tab = [randrange(1,100) for i in range(n)]
print("Tableau à trier : ")
for k in range(n):
    print(Tab[k],"\t",end=' ')

for k in range(1,n):
    for i in range(k):
        if Tab[i]>Tab[k]:
            Tab[i] = Tab[i] + Tab[k]
            Tab[k] = Tab[i] - Tab[k]
            Tab[i] = Tab[i] - Tab[k]
print("\n")
print("Tableau trié : ")
for k in range(n):
    print(Tab[k],"\t",end=' ')
