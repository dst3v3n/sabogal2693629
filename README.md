# sabogal2693629

[![Python](https://img.shields.io/badge/Python-1.11.3+-802DBF?style=for-the-badge&logo=python&logoColor=802DBF&labelColor=black)](https://www.python.org/)
[![Visual-Studio-Code](https://img.shields.io/badge/visual_studio_code-1.78+-802DBF?style=for-the-badge&logo=visual-studio-code&logoColor=802DBF&labelColor=black)](https://code.visualstudio.com/)

## Aprendiendo los fundamentos de Python

### El proyecto lo estoy realizando en el SENA. Estoy estudiando un tecnologo en Analisis y Desarrollo de Software (ADSO) :purple_heart: 

--------

>Contenido de los ejercicios con la documentación del proyecto


|# Files | Topics                                                    |
|------|:---------------------------------------------------------:|
| 00  |  [Introduction](./intro/intro1.py)||
| 01  |  [Condicionales](./condicionales)|
| 02  |  [Bucles](./bucles)
| 03  |  [lista](./lista)|
| 04  |  [funciones](./funciones)|
| 05  |  [tuplas](./tuplas)|
| 06  |  [diccionario](./diccionario)|

--------
## **Ultimos codigos realizados** :purple_heart:

```python
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
        z=round(((x+y)/2),2)
        return z
    else:
        quintile=int(valor*len(lista)/5)
        mayor=int(quintile)
        menor=int((valor-1)*len(lista)/5)
        listaQuin=lista[menor:mayor]
        return(listaQuin)

    
def cuartiles(lista,valor):
    quintile=int(valor*len(lista)/4) 
    if len(lista)%4!=0:
        x=lista.pop(quintile)
        y=lista.pop(quintile+1)
        z=round(x+y/2,2)
        return z
    else:
        quintile=int(valor*len(lista)/4)
        mayor=int(quintile)
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
```
>El codigo se encuentra **[Aqui](./funciones/funcion7.py)**

------
## Seguire aprendiendo mas acerca del mundo de **python!**. Este es solo el principio:purple_heart:

--------
#### Puedes apoyar mi trabajo haciendo "☆ Star" en el repo. ¡Gracias!

 ### Hola, mi nombre es Harold Sabogal.
### Estudiante del SENA

![GitHub Followers](https://img.shields.io/github/followers/dst3v3n?style=social)
![GitHub Followers](https://img.shields.io/github/stars/dst3v3n?style=social)

Soy estudiante del SENA desde hace dos año. Este años estoy aprendiendo sobre Analisis y Desarrollo de Software (ADSO) como lo he comentado anteriormente, lo estoy estudiando en el SENA. Quiero seguir aprendiendo mas sobre el mundo del Desarrollo de software **[@dst3v3n](https://github.com/dst3v3n)**.

### En mi perfil de GitHub tienes más información

[![Web](https://img.shields.io/badge/Guthub-dst3v3n-802DBF?style=for-the-badge&logo=github&logoColor=802DBF&labelColor=black)](https://github.com/dst3v3n)
