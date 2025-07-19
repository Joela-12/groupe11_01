texte = input("Entrez une chaine : ")
inverse = ""

for char in texte :
    inverse = char + inverse

print(f"Chaine inversée : {inverse}")