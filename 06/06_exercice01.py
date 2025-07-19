import random

nombre_secret = random.randint(1,100)
essaie = None

while essaie != nombre_secret:
    essaie = int(input("Devine le nombre (1-100) : "))
    if essaie < nombre_secret:
        print("Trop petit.")
    elif essaie > nombre_secret:
        print("Trop grand.")
    else:
        print("Bravo, tu as trouvé !")