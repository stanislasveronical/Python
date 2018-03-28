def ecrire_matrice(Mat):
    for i in range (3):
        print(Mat[i],"\t")
Mat = [[i+j*3+1 for i in range(3)] for j in range(3)]
print("La matrice Mat est : ",end="")
ecrire_matrice(Mat)
