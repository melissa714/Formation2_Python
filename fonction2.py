def moyenne(x,*args): 
    """Calcule la moyenne d'un nombre quelconque de valeurs passées en parametre"""
    nb= 1 + len(args)
    print(len(args))
    somme=x 
    for y in args:
        somme += y 
    return somme / nb 


resultat=moyenne(1,5,8)
print(resultat)


def afficher_params(**kwargs):
    """affiche tous les parametres nommés passés en parametre"""
    for k,v in kwargs():
        print(k,":",v)

afficher_params(prenom="tre",age=15)