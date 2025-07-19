def calculer (a, b, op):
    if op== "+" :
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op== "/":
        if b != 0 :
            return a/ b
        else :
            return "Division par zéro impossible."
    else :
        return "Opérateur non valide."
# Exemple d'utilisarion
x = float (input ( "Nombre: " ))
y = float (input ( "Nombre 2: "))

operation = input ("Opération (+, -, *, /) : ")

resultat = calculer(x, y, operation)
print (f"Résultat : {resultat}")
