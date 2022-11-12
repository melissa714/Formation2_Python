def demander_nom():
    nom=input("entrez le nom svp:",)
    return nom


def afficher(*args):
    print(*args)
    print(__name__)


if __name__ == 'main':
    nom=demander_nom()
