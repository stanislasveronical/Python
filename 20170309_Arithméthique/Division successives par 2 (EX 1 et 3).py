#EXERCICE 1

n= int(input("Entrer l'entier à convertir : "))
bin , q = [ ],n
while q//2 !=0:
    bin = [q%2] + bin
    q = q//2
bin = [q%2] + bin
print("L'écriture binaire de l'entier",n,"est ")
for k in range(len(bin)):
    print(bin[k],end=' ')



#EXERCICE 3 : Conversion Inverse

print("\n")   
bin , n = input("Entrer l'écriture binaire à convertir : "),0
for k in range(len(bin)): 
    n = n + int(bin[len(bin)-1-k])* 2**(k)
print("L'entier dont l'écriture binaire est ",bin, "est égal à", n)
