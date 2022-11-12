
while True:
    try:
        nombre = int(input("saisir un nombre svp:"))
    except ValueError:
        print("desolé ce n est pas un nombre")
        continue
    else:
        print("le nombre est:", nombre)
    break