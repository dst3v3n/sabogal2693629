#Llenar dos arreglos de n elementos con números generados con la función random.
#Compararlos y decir:
#a. Cuál de los dos tiene la suma más alta
#b. Cuál de los dos tiene el número mayor
#c. Cuál de los dos tiene el número menor
#d. Cuál es el promedio conjunto (uniendo los dos arreglos)
#e. Sacar el promedio de cada uno y decir si está por encima o por debajo del arreglo conjunto
#f. Cuál de los dos tiene mayor cantidad de pares
#g. Cuál de los dos tiene mayor cantidad de impares

import random

lista1=[random.randrange(100) for i in range(random.randint(20,25))]
lista2=[random.randrange(100) for i in range(random.randint(20,25))]
suma1=0
suma2=0
par1=0
par2=0
impar1=0
impar2=0

print(f"Primera lista {lista1}" )
print(f"Segunda lista {lista2}" )

for i in lista1:
    suma1+=i
for j in lista2:
    suma2+=j
if suma1>suma2:
    print(f"La primera lista tiene una suma mayor {suma1}")
if suma1<suma2:
    print(f"La segunda lista tiene una suma mayor {suma2}")

for i in range (len(lista1)):
    for j in range(i+1,len(lista1)):
        if lista1[i]>lista1[j]:
            aux1=lista1[i]
            lista1[i]=lista1[j]
            lista1[j]=aux1

for i in range (len(lista2)):
    for j in range(i+1,len(lista2)):
        if lista2[i]>lista2[j]:
            aux2=lista2[i]
            lista2[i]=lista2[j]
            lista2[j]=aux1       
menor1=lista1.pop(0)
menor2=lista2.pop(0)
mayor1=lista1.pop(-1)
mayor2=lista2.pop(-1)   

if menor1>menor2:
    print(f"{menor2} El numero menor es el de la lista 2")
elif menor1<menor2:
    print(f"{menor1} El numero menor es el de la lista 1")
else:
    print("Las listas tienen el mismo numero menor")


if mayor1>mayor2:
    print(f"{mayor1} El numero mayor es el de la lista 1")
elif mayor1<mayor2:
    print(f"{mayor2} El numero mayor es el de la lista 2")
else:
    print("Las listas tienen el mismo numero mayor")

suma_total=suma1+suma2
longitud=len(lista1)+len(lista2)
promedio=suma_total/longitud

print(f"El promedio total de las dos listas es: {promedio}")

promedio1=suma1/len(lista1)
promedio2=suma2/len(lista2)

if promedio1>promedio:
    print(f"El promedio de la lista 1 esta por encima del promedio total {promedio1}")
else:
    print(f"El promedio de la lista 1 esta por debajo del promedio total {promedio1}")

if promedio2>promedio:
    print(f"El promedio de la lista 2 esta por encima del promedio total {promedio2}")
else:
    print(f"El promedio de la lista 2 esta por debajo del promedio total {promedio2}")

for i in lista1:
    if i%2==0:
        par1+=1
    else:
        impar1+=1

for i in lista2:
    if i%2==0:
        par2+=1
    else:
        impar2+=1

if par1>par2:
    print(f"{par1} Hay mas numeros par en la lista 1 ")
elif par1<par2:
    print(f"{par2} Hay mas numeros par en la lista 2 ")
else:
    print(f"Hay igual cantidad de pares en cada lista")

if impar1>impar2:
    print(f"{impar1} Hay mas numeros impar en la lista 1 ")
elif impar1<impar2:
    print(f"{impar2} Hay mas numeros impar en la lista 2 ")
else:
    print(f"Hay igual cantidad de impares en cada lista")