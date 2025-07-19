age = int(input("Entrez votre age : "))
pays = input("Entrez votre pays : ").lower()
if age >= 18 and (pays == "congo" or pays == "cameroun"):
    print("Inscription autorisée.")
elif age < 18 :
    print("Vous etes trop jeune pour vous inscrire.")
else:
    print("Désolé, programme réservé aux ressortissants du Congo ou Cameroun.")