nombre=input("entrez le nombre:")

try:
    nombre=int(nombre)
except ValueError as e:
    print(e)