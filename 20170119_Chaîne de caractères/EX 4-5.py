phrase = input("Entrer une phrase à tester : ").upper()
renverse = ''
for car in phrase:
    renverse = car + renverse
print(renverse)




phrase , phrase1 = input("Entrer une phrase à tester :").upper(),""
phrase_inversée = ""
for lettre in phrase:
    if lettre != " ":
        phrase1 = phrase1 + lettre
        phrase_inversée = lettre + phrase_inversée
print(phrase1)
print(phrase_inversée)

if phrase1 == phrase_inversée:
    print("La phrase,",phrase,"est un palindrome.")
else:
    print("La phrase,",phrase,"n'est pas un palindrome.")
    for k in range(len(phrase1)):
        if phrase1[k]!=phrase_inversée[k]:
            print("La première lettre diffèrente est celle en position : ", k)
            break
