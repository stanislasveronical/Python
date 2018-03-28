N = int(input("Entrer l'entier à tester : "))
d , div =2 , [1]
while d<= N:
    if N%d ==0:
        div = div + [d]
    d+=1
if len(div) == 2:
    print("L'entier ",N,"est un nombre premier.")
else:
    print("L'entier ",N,"n'est pas un nombre premier.")
    print("Il possède ",len(div),"diviseurs dont voici la liste:")
    for i in range (len(div)):
        print(div[i],end="  ")
        
