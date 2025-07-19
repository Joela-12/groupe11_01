texte = input("Entrez un texte : ").lower()
mot = input("Mot à chercher : ").lower()

compte = texte.count(mot)

print(f"Le mot '{mot}' apparait {compte} fois.")