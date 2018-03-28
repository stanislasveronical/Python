n= int(input("Saisir un nombre : ")) 
compteur = 1	
while compteur <= 10:
    
    print(n, "*", compteur," = ", compteur*n)
    compteur = compteur + 1   




n = int(input("Entrer n = "))
k = int(input("Combien de multiples ? k = "))

for i in range (1,k+1):
    print (i,"x" ,n, "=" , i*n)
    
