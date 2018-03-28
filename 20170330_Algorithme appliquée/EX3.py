def contraste(Mat,luminosite):
    for i in range (len(Mat)):
            if Mat[i]<lum:
                Mat[i]=Mat[i]/2
            else:
                if 2*Mat[i]<100:
                    Mat[i] =2*Mat[i]
                else:
                    Mat[i] =100
contraste(Mat,luminosite)
