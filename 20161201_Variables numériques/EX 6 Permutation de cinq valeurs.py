a=int(input('saisir a :'))
b=int(input('saisir b :'))
c=int(input('saisir c :'))
d=int(input('saisir d :'))
e=int(input('saisir e :'))

a=a+c
b=b+a
b=b-c
c=c+e
e=c-e
c=c-e
d=d-b
e=e+a
e=e-c

print("la valeur de a est", a)
print ("la valeur de b est", b)
print("la valeur de c est", c)
print ("la valeur de d est", d)
print ("la valeur de e est", e)
