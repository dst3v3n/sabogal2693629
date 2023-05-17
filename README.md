# sabogal2693629

[![Python](https://img.shields.io/badge/Python-1.11.3+-802DBF?style=for-the-badge&logo=python&logoColor=802DBF&labelColor=black)](https://www.python.org/)
[![Visual-Studio-Code](https://img.shields.io/badge/visual_studio_code-1.78+-802DBF?style=for-the-badge&logo=visual-studio-code&logoColor=802DBF&labelColor=black)](https://code.visualstudio.com/)

## Aprendiendo los fundamentos de Python

### El proyecto lo estoy realizando en el SENA. Mi ficha 2693629 ADSO Cadena de Formacion

--------

### Contenido de los ejercicios con la documentación del proyecto


|# Files | Topics                                                    |
|------|:---------------------------------------------------------:|
| 00  |  [Introduction](./intro/intro1.py)||
| 01  |  [Condicionales](./condicionales)|
| 02  |  [Bucles](./bucles)
| 03  |  [lista](./lista)|
| 04  |  [funciones](./funciones)|

--------
## **Ultimos codigos realizados**

```python
import random

def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def compararSuma (lista1,lista2):
    suma1=sumaLista(lista1)
    suma2=sumaLista(lista2)
    if suma1>suma2:
        mayor=suma1
        return mayor
    elif suma2>suma1:
        mayor=suma2
        return mayor
    else:
        return f"La suma de los numeros son iguales"
    
def ordenAscen(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]>lista[j]:
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux 
    return lista

def promedioConjunto(lista1,lista2):
    suma1=sumaLista(lista1)
    suma2=sumaLista(lista2)
    suma_total=suma1+suma2
    promedio= suma_total/(len(lista1)+(len(lista2)))
    return promedio

def promedio(lista):
    suma=0
    for x in lista:
        suma+=x
    promedio= suma/(len(lista1))
    return promedio

def promedioLista(lista1,lista2):
    promedioCon= promedioConjunto(lista1,lista2)
    promedio1= promedio(lista1)
    if promedio1>promedioCon:
        return f"El promedio esta por encima del promedio Conjunto"
    elif promedio1<promedioCon:
        return f"El promedio esta por debajo del promedio Conjunto"
    else:
        return f"El promedio es igual"
    
def pares (lista1,lista2):
    par1=0
    par2=0
    for i in lista1:
        if i%2==0:
            par1+=1
    for i in lista2:
        if i%2==0:
            par2+=1
    if par1>par2:
        return f"{par1} Hay mas numeros par en la lista 1"
    elif par2>par1:
        return f"{par2} Hay mas numeros par en la lista 2"
    else:
        return "Hay igual cantidad de pares en las dos listas"
def impares(lista1,lista2):
    impar1=0
    impar2=0
    for i in lista1:
        if i%2!=0:
            impar1+=1
    for i in lista2:
        if i%2!=0:
            impar2+=1
    if impar1>impar2:
        return f"{impar1} Hay mas numeros impar en la lista 1"
    elif impar2>impar1:
        return f"{impar2} Hay mas numeros impar en la lista 2"
    else:
        return "Hay igual cantidad de impares en las dos listas"

def numMayor(lista1,lista2):
    mayor1=lista1.pop(-1)
    mayor2=lista2.pop(-1)
    if mayor1>mayor2:
        return(mayor1)
    elif mayor2>mayor1:
        return(mayor2)
    else: 
        return f"Los numero mayores son iguales"
    
def numMen(lista1,lista2):
    menor1=lista1.pop(0)
    menor2=lista2.pop(0)
    if menor1<menor2:
        return(menor1)
    elif menor2<menor1:
        return(menor2)
    else: 
        return f"Los numero menores son iguales"


lista1=llenarLista(15,25)
lista2=llenarLista(15,25)

ordenAscen(lista1)
ordenAscen(lista2)

print("1-Suma de cada lista")
print("2-Comparar las dos sumas")
print("3-Promedio Conjunto")
print("4-Promedio de cada lista")
print("5-Comparar el promedio de las dos listas")
print("6-Impar de los listas")
print("7-Par de los listas")
print("8-Numero mayor de las dos listas")
print("9-Numero menor de las dos listas")
selector=1
while selector!=0:
    selector=input("Digite la opcion: ")
    match selector:
        case "1":
            print("Lista 1",lista1)
            print("Lista 2",lista2)
            print("Suma de la lista 1",sumaLista(lista1))
            print("Suma de la lista 2",sumaLista(lista2))
        case "2":
            print("Lista 1",lista1)
            print("Lista 2",lista2)
            print("La suma mayor de la lista es: ",compararSuma(lista1,lista2))
        case "3":
            print("Promedio de las dos lista",promedioConjunto(lista1,lista2))
        case "4":
            print("Promedio de la lista 1",promedio(lista1))
            print("Promedio de la lista 2",promedio(lista2))
        case "5":
            print(promedioLista(lista1,lista2))
            print(promedioLista(lista2,lista1))
        case "6":
            print(impares(lista1,lista2))
        case "7":
            print(pares(lista1,lista2))
        case "8":
            print("Lista 1",lista1)
            print("Lista 2",lista2)
            print(numMayor(lista1,lista2))
        case "9":
            print("Lista 1",lista1)
            print("Lista 2",lista2)
            print(numMen(lista1,lista2))
        case "0":
            break
```
>El codigo se encuentra **[Aqui](./funciones/funcion5.py)**

```python
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
    mayor=int(quintile)
    menor=int((valor-1)*len(lista)/5)
    if len(lista)>=quintile:
        listaQuin=lista[menor:mayor]
        return listaQuin
    else: 
        return f"No se puede hallar el quintil"

lista1=llenarLista(100,1.79)
print(ordenAscen(lista1))
print(len(lista1))
x=1

while x!=0:
    x=abs(int(input("Digita que quintil quieres hallar: ")))
    if x>=1 and x<=5:
        print(quintiles(lista1,x))
    elif x==0:
        print("Haz salido correctamente del programa")
    else:
        print("Este numero es invalido")

```
>El codigo se encuentra **[Aqui](./funciones/funcion6.py)**

------
## Seguire aprendiendo mas acerca del mundo de python!. Este es solo el principio:earth_africa::purple_heart:

--------
#### Puedes apoyar mi trabajo haciendo "☆ Star" en el repo. ¡Gracias!

 ### Hola, mi nombre es Harold Sabogal.
### Estudiante del SENA

![GitHub Followers](https://img.shields.io/github/followers/dst3v3n?style=social)
![GitHub Followers](https://img.shields.io/github/stars/dst3v3n?style=social)

Soy estudiante del SENA desde hace dos año. Este años estoy aprendiendo sobre Analisis y Desarrollo de Software (ADSO) como lo he comentado anteriormente, lo estoy estudiando en el SENA. Quiero seguir aprendiendo mas sobre el mundo del Desarrollo de software **[@dst3v3n](https://github.com/dst3v3n)**.

### En mi perfil de GitHub tienes más información

[![Web](https://img.shields.io/badge/Guthub-dst3v3n-802DBF?style=for-the-badge&logo=github&logoColor=802DBF&labelColor=black)](https://github.com/dst3v3n)
