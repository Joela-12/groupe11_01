entree = input("Entrez des nombres séparés par des espaces : ")
liste = entree.split()

elements_pairs = liste[::2]

print(f"Eléments aux indices pairs : {elements_pairs}")