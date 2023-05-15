import random

def llenarLista(tam,rango):
    tama=1
    while tama%5!=0:
        tama=random.randint(15,tam)
        lista=[random.uniform(1.50,rango) for i in range(tam)]    
    return lista


lista1=llenarLista(100,1.79)
print(lista1)