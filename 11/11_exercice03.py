def est_palindrome (mot):
    return mot== mot[::-1]

mot= input ("Entrez un mot : ")
if est_palindrome(mot):
    print ("c'est un palindrome." )
else :
    print ("ce n'est pas un palindrome." )
