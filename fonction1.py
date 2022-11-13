t=[20,20]
resultat,reste=divmod(*t)
print(resultat,reste)


d = {"nom": "Gayerie", "prenom": "David"}

s = ["david"]
a = {"nom": "Gayerie"}

def dire_bonjour_a(prenom, nom):
    print("bonjour",prenom,nom)
dire_bonjour_a(**d)
dire_bonjour_a(*s,**a)