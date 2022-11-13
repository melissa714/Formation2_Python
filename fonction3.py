def fonction_libre(*args,**kwargs):
    pass 


# Appel récursif de fonction

def appel_recursif():
    """ si vous appelez  cette fonction,elle fera échouer votre programme"""
    appel_recursif()

def factorielle(n):
    if n>0:
        return n * factorielle(n-1)
    else:
        return 1

fact=factorielle(6)
print(fact)


# Déclaration de fonction dans une fonction

def outter(message):
    def inner():
        print(message)
    inner()

outter("hello")




def outer(prenom):
    message=None
    def inner():
        # la variable message n est pas local
        nonlocal message
        message="Bonjour %s" % prenom 
    inner()
    print(message) 

outter("clarice")
  



def neg(x): return -x
print(neg(1))


def somme(x, y): return x + y
print(somme(2, 3))
