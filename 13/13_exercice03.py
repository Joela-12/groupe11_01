nom_fichier = input ("Nom du fichier à lire :")

try :
    with open (nom_fichier, "r" , encoding="utf-8" ) as f:
        contenu= f.read()
except FileNotFoundError:
    print ("Erreur: Fichier introuvable." )
else :
    print ("contenu du fichier:" )
    print (contenu)
