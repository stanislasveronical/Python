a = int(input(" Saisir a : "))
b = int(input(" Saisir b : "))

def pgcd(a,b) :  
   while a%b != 0 : 
      a, b = b, a%b 
   return b
print (pgcd (a,b))
