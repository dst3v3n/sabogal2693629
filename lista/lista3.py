import random
tam=random.randint(5,10)
lista=[random.randrange(100) for i in range(tam)]
suma=0
sumae=0
resta=[]
elevado=[]
print(lista)
print(tam)
for i in range(tam):
    for j in range(i+1,tam):
        if lista[i]>lista[j]:
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
print("Lista en orden",lista)

if len(lista)%2==0:
    mediana = (lista[(tam // 2) - 1] + lista[tam // 2]) / 2
else: 
    mediana=lista[(len(lista)//2)]

for i in lista:
    suma+=i
media=(suma/tam)
ind=0
for i in lista:
    cont=0
    for f in lista:
        if i==f:
            cont+=1
    if cont==1:
        print("No hay moda, no hay datos repetidos")
    if cont>ind:
        ind=cont
        moda=i

for i in lista:
    y=((i-media))
    resta.append(y)
for j in resta:
    y=((j**2))
    elevado.append(y)
for y in elevado:
    sumae+=y
diviv=(sumae/tam-1)

ds=diviv**0.5

print(f"La mediana de la lista es: {mediana}")
print(f"la media de la lista es: {media}")
print(f"La moda de la lista es: {moda}")
print(f"La desviacion Estandar de la lista es: {ds}" )
