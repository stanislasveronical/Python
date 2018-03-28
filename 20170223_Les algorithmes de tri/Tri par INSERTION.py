from random import*
n = int(input("Entrer le nombre de données à trier : "))
Tab = [randrange(1,100) for i in range(n)]
for k in range(n):
    print(Tab[k],"\t",end=' ')

for k in range(1,n):
    for i in range(k):
        if Tab[i]>Tab[k]:
            for j in range(i,k):
                Tab[j] = Tab[j] + Tab[k]
                Tab[k] = Tab[j] - Tab[k]
                Tab[j] = Tab[j] - Tab[k]
print("Tableau trié : ")
for k in range(n):
    print(Tab[k],"\t",end=' ')



#Module Echange

from random import*
from echange import*
n = int(input("Entrer le nombre de données à trier : "))
Tab = [randrange(1,100) for i in range(n)]
for k in range(n):
    print(Tab[k],"\t",end=' ')

for k in range(1,n):
    for i in range(k):
        if Tab[i]>Tab[k]:
            for j in range(i,k):
                (Tab[j],Tab[k]) = echange(Tab[j],Tab[k])
print("Tableau trié : ")
for k in range(n):
    print(Tab[k],"\t",end=' ')
