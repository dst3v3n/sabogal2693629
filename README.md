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
| 07  |  [excepciones](./excepciones)|

--------
## **Ultimos codigos realizados** :purple_heart:

```python
def usarEspañol (diccionario , x ):
    if x in diccionario:
        return diccionario[x]


def usarIngles (diccionario , x):
    if x in diccionario:
        return diccionario[x]

def updateEspañol(diccio , x , y ):
    diccio.update({x : y})
    return diccio

def updateIngles(diccio , x , y):
    diccio.update({x : y})
    return diccio


def tuplaEspañol(tupla,x):
    tupla = tupla + (x,)
    print(tupla)
    return tupla

def tuplaIngles(tupla,x):
    tupla = tupla + (x,)
    return tupla


español = {}
ingles={}
spanish = ()
english = ()


print("1.Mostrar diccionario en Español Ingles")
print("2.Mostrar diccionario en ingles Español")
print("3.Agregar diccionario de Español")
print("4.Agregar diccionario de Ingles")
print("5.Usar Diccionario de Español")
print("6.Usar Diccionario de Ingles")

selector = 1

while selector !=0:
    selector = abs(int(input("Digita una opcion: ")))
    match selector:
        case 1:
            print(español)
            print(spanish)
        case 2:
            print(ingles)
            print(english)
        case 3:
            clave = str(input("Digita la palabra en español que quieres agregar: "))
            valor = str(input("Digita la palabra en ingles que quieres agregar: "))
            print(updateEspañol(español,clave,valor))
            spanish=tuplaEspañol(spanish,clave)
        case 4:
            clave = str(input("Digita la palabra en ingles que quieres agregar: "))
            valor = str(input("Digita la palabra en español que quieres agregar: "))
            print(updateIngles(ingles,clave, valor))
            english=tuplaEspañol(english,clave)
        case 5:
            x= input("Ingresa la palabra ")
            print(usarEspañol(español,x))
        case 6:
            x= input("Ingresa la palabra ")
            print(usarIngles(ingles,x)) 
```
>El codigo se encuentra **[Aqui](./diccionario/diccio5.py)**

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
