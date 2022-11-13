def trace(func):
    def decorateur(*args, **kwargs):
        print("Début d'appel à", func)
        resultat = func(*args, **kwargs)
        print("Fin d'appel à", func)
        return resultat
    return decorateur


@trace
def moyenne(x, *args):
    """Calcule la moyenne d'un nombre quelconque de valeurs passées en paramètres."""
    nb = 1 + len(args)
    somme = x
    for y in args:
        somme += y
    return somme / nb


print(moyenne(1, 2, 3))
