
moy1=float(input("entrez la premiere moyenne: "))
moy2=float(input("entrez la deuxieme moyenne: "))
moy_total=(moy1+moy2)/2

if moy_total>=10:
    print("felication vous avez validé avec {}".format(moy_total))
elif moy_total<10:
    print("désole vous n'avez pas validé ,votre moyenne est {}".format(moy_total))
else:
    print("je ne sais heinnn")
