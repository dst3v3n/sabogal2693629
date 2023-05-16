# minimo 15 maximo 125.{validación}
# Llenar lista {Estaturas. 1,50 - 2,00}
# Hallar Quintiles (impriman los percentiles en rango)

import random

def llenarLista(tamaño,rango):
    tama=random.randint(15,tamaño)
    while tama==tama:
        tama=random.randint(15,tamaño)
        if tama%5==0:
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
    quintile=valor*len(lista)/5
    menor=int(quintile-6)
    mayor=int(quintile)
    if len(lista)>=quintile:
        listaQuin=lista[menor:mayor]
        return listaQuin
    else: 
        return f"No se puede hallar el quintil"

lista1=llenarLista(100,1.79)
print(ordenAscen(lista1))
print(len(lista1))
x=abs(int(input("Digita que quintil quieres hallar: ")))
print(quintiles(lista1,x))