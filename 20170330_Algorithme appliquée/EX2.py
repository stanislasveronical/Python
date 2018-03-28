def luminosite(Mat):
    somme =0
    for i in range (len(Mat)):
        somme = somme +Mat[i]
        lum =somme/len(Mat)
        return(lum)
Mat = eval (input("Entrer la matrice : "))
print(Mat)
print("La luminosité de l'image vaut : ",luminosite(Mat))
