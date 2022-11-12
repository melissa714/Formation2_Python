
nombre=input("entrez un nombre:")
try:
    nombre=int(nombre)
except ValueError:
    print("ce n est une valeur decimal que vous avez entré")
else:
    print(nombre)