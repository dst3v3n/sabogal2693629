#LLenar una lista con numero aleatorios (reales con un decimal) que presenten calificaciones
#de un curso. Se evalua de 0 a 5. Ej 
#El curso puede tener entre 20 y 30 aprendices.
#Hallar 
#1. genero listas nuevas para los aprobados y los reprobados(Se aprueba con 3) 
#2. Genere listas nuevas por cadaa unidad. Es decir , los que sacan de 0 a 1 son un grupo los de 1 a 2 otro grupo y asi sucesivamente
#3. Diga cual es el promedio de los que aprueban y de los que reprueban por separado

import random

lista=[float(random.randrange(6)) for i in range(random.randint(20,30))]
suma_repro=0
print(lista)

for i in range(len(lista)):
    for j in range(i+1,len(lista)):
        if lista[i]>lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
print("Lista en orden",lista)

for j in lista:
    if j==3.0:
        posicion=(lista.index(j))
    if j==2.0:
        posicion1=(lista.index(j))
    if j==4.0:
        posicion2=(lista.index(j))
unidad1=lista[:posicion1]
unidad2=lista[posicion1:posicion2]
unidad3=lista[posicion2:] 
aprobado=lista[posicion:]
reprobado=lista[:posicion]

for i in lista:
    if i<3.0:
        suma_repro+=i

print(f"Aprobados: {aprobado}")
print(f"Reprobados: {reprobado}")
print(f"Unidad 1: {unidad1}")
print(f"Unidad 2: {unidad2}")
print(f"Unidad 3: {unidad3}")
print(f"Suma {suma_repro}")


