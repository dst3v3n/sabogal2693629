# * minimo 15 maximo 125.{validación} Incluir todos los numeros
# * Llenar lista {Estaturas. 1,50 - 2,00} - función
# * hacer una función que encuentre todos los cuartiles y otra función para todos los quintile
# * Hallar cuadriles y quintiles (impriman los percentiles en rango)

import random

def llenarLista(tamaño,rango):
    tama=random.randint(15,tamaño)
    lista=[round(random.uniform(1.50,rango),2) for i in range(tama)]   
    return lista

def ordenAscen(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux 
    return lista
        
def quintiles(lista,valor):
    quintile=int(valor*len(lista)/5)
    print(quintile) 
    if len(lista)%5!=0:
        x=lista.pop(quintile)
        y=lista.pop(quintile+1)
        lista.insert(quintile,x)
        lista.insert(quintile+1,y)
        z=round(((x+y)/2),2)
        return z
    else:
        quintile=int(valor*len(lista)/5)
        mayor=int(quintile)
        menor=int((valor-1)*len(lista)/5)
        listaQuin=lista[menor:mayor]
        return(listaQuin)

    
def cuartiles(lista,valor):
    cuartile=int(valor*len(lista)/4) 
    if len(lista)%4!=0:
        x=lista.pop(cuartile)
        y=lista.pop(cuartile+1)
        lista.insert(cuartile,x)
        lista.insert(cuartile+1,y)
        z=round(x+y/2,2)
        return z
    else:
        cuartile=int(valor*len(lista)/4)
        mayor=int(cuartile)
        menor=int((valor-1)*len(lista)/4)
        listaQuin=lista[menor:mayor]
        return(listaQuin)

lista1=llenarLista(125,1.79)
print(ordenAscen(lista1))
print(len(lista1))
x=1

while x!=0:
    x=abs(int(input("Digita que quintil y cuartil quieres hallar: ")))
    if x>=1 and x<=5:
        print("Quintiles",quintiles(lista1,x))
        print("Cuartiles",cuartiles(lista1,x))
    elif x==0:
        print("Haz salido correctamente del programa")
    else:
        print("Este numero es invalido")