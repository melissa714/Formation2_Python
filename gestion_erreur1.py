# nombre=input("entrez le nombre:")

# try:
#     nombre=int(nombre)
# except ValueError as e:
#     print(e)


try:
    numerateur = int(input("Entrez un numérateur : "))
    denominateur = int(input("Entrez un dénominateur : "))
    resultat = numerateur / denominateur
    print("Le resultat de la division est", resultat)
except (ValueError, ZeroDivisionError):
    print("Désolé, quelque chose ne s'est pas bien passé.")
else:
    print(resultat)