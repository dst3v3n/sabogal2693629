#Llenar un arreglo de n elementos con números generados con la función random. N es
#ingresado por el usuario. Diseñe un menú con las siguientes operaciones.
#a. Imprimir arreglo original (El primero que se generó)
#b. Suma
#c. Promedio
#d. Mayor
#e. Menor
#f. Ordenar ascendente (No perder el arreglo original; el del punto a)
#g. Ordenar descendente (No perder el arreglo original; el del punto a)
#h. Moda
#i. Mediana
#j. Buscar. Decir si encuentra el número, en qué posición(es) está, cuantas veces está

import random

def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista

def sumaLista(lista):
    suma=0
    for x in lista:
        suma+=x
    return suma

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

def mayor(lista):
    mayor=0
    for i in lista:
        if i>mayor:
            mayor=i
    return mayor

def menor(lista):
    menor=100000000
    for i in lista:
        if i<menor:
            menor=i
    return menor

def ordenAscen(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux 
    return lista

def ordenDesce(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]<lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux 
    return lista

def modaLista(lista):
    ind=0
    for i in lista:
        cont=0
        for f in lista:
            if i==f:
                cont+=1
        if cont>ind:
            ind =cont
            moda=i
    return moda

def medianaLista(lista):
    if len(lista)%2==0:
        mediana=(lista[(len(lista)//2)-1]+ lista[len(lista)//2])/2
    else:
        mediana =lista[(len(lista)//2)]
    return mediana


def buscarLista(lista,x):
    cont=0
    if x in lista:
        for i in range(len(lista)):
            if x==lista[i]:
                cont+=1
        return f"El numero existe {cont} veces"
    else:
        return "El numero no existe"
            
lista=llenarLista(15,25)
print(lista)
print(sumaLista(lista))
print(round(promedioLista(lista),2))
print(mayor(lista))
print(menor(lista))
print(ordenAscen(lista))
print(ordenDesce(lista))
print(modaLista(lista))
print(medianaLista(lista))
num=int(input("Digite un numero: "))
print(buscarLista(lista,num))