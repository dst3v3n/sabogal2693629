# sabogal2693629

[![Python](https://img.shields.io/badge/Python-1.11.3+-802DBF?style=for-the-badge&logo=python&logoColor=802DBF&labelColor=black)](https://www.python.org/)
[![Visual-Studio-Code](https://img.shields.io/badge/visual_studio_code-1.78+-802DBF?style=for-the-badge&logo=visual-studio-code&logoColor=802DBF&labelColor=black)](https://code.visualstudio.com/)

## Aprendiendo los fundamentos de Python

### El proyecto lo estoy realizando en el SENA. Estoy estudiando un tecnologo en Analisis y Desarrollo de Software (ADSO) :purple_heart: 

--------

>Contenido de los ejercicios con la documentación del proyecto


|# Files | Topics                                                    |
|------|:---------------------------------------------------------:|
| 00  |  [Introducción](./intro/intro1.py)||
| 01  |  [Condicionales](./condicionales)|
| 02  |  [Bucles](./bucles)
| 03  |  [Lista](./lista)|
| 04  |  [Funciones](./funciones)|
| 05  |  [Tuplas](./tuplas)|
| 06  |  [Diccionario](./diccionario)|
| 07  |  [Excepciones](./excepciones)|
| 08  |  [Modulos](./modulos)|
| 09  |  [Objetos](./objetos)|
| 10  |  [Herencia](./herencia)|
| 11  |  [Ejercicio Herencia](./herencia/library_python)|
| 12  |  [Pruebas Modulos](./pruebas/modulos)|
| 13  |  [Pruebas Objetos](./pruebas/objetos/)|

--------
## **Ultimos codigos realizados** :purple_heart:

>Programación Orientada a Objetos

```python
from sys import path

path.append("..\\sabogal2693629")

from herencia.library_python.Account import *
from herencia.library_python.Book import *


class User(Account):
    def __init__(self , Name:str , ID:int):
        self._name = Name
        self.__id = ID
        self.__verificado = None
        Account.__init__(self , Name , ID)
        Book.__init__(self , "La llorona" , "Harold" , 102866 , "10/25/2014" , "Harold")

    def verify (self , Name:str, ID:int):
        if self._name == Name and self.__id == ID:
            self.__verificado = "Verificado"
            return "Verificado"
        else:
            self.__verificado = "No Verificado"
            return "No Verificado"
            
    def LibroReservado (self ,Name:str , Titulo:str):
        self._reservado.append(Titulo)
        self._libros.append (Titulo)
        del self._obj_titulo1[Name]
        self._obj_titulo1.update ({Name : self._libros + [Titulo]})
        Book.Obj_Libro(self,Name,Titulo)
        
    def LibroDevuelto (self ,Name:str , Titulo:str):
        self._devuelto.append(Titulo)
        self._libros.append (Titulo)
        del self._obj_titulo1[Name]
        self._obj_titulo1.update ({Name : self._libros + [Titulo]})
        Book.Obj_Libro(self,Name,Titulo)
        
    def LibroPerdido (self , Name:str, Titulo:str):
        self._perdido.append(Titulo)
        self._libros.append (Titulo)
        del self._obj_titulo1[Name]
        self._obj_titulo1.update ({Name : self._libros + [Titulo]})
        Book.Obj_Libro(self,Name,Titulo)
        self.setMulta(len(self._perdido))

    def CheckAccount (self, Name:str):
        return self._obj_titulo1[Name]
        
    def get_book_info (self , Titulo:str , informacion):
        self.__informacion = informacion
        print(self.__informacion[Titulo])
```
>El codigo se encuentra **[Aqui](./herencia/library_python/User.py)**

--------
>App Libreria



```python
from sys import path

path.append("..\\sabogal2693629")

from herencia.library_python.Book import *
from herencia.library_python.Account import *
from herencia.library_python.User import *


obj2 = Book ("La llorona" , "Harold" , 102866 , "10/25/2014" , "Harold")
obj1 = User ("Harold" , 102866)
obj3 = Account ("Harold" , 102866)


obj1.LibroReservado("Harold","La llorona")
obj1.LibroReservado("Harold","La guerra de los cielos" )
obj1.LibroDevuelto("Harold","La llorona")
obj1.LibroDevuelto("Harold","La guerra de los cielos")
obj1.LibroPerdido("Harold"," La llorona")
obj1.LibroPerdido("Harold", "La Guerra de los cielos")
obj1.LibroPerdido("Harold", "La guerra de los cielos")
obj1.LibroPerdido("Harold", "La guerra de los cielos")

obj3.setMulta (5)
print("multa",obj3.calculate_fine())

print(obj1.CheckAccount("Harold"))

obj1.get_book_info ("La llorona" , obj2._informacion)
```
>El codigo se encuentra **[Aqui](./pruebas/objetos/LibraryAPP.py)**

------
## Seguire aprendiendo mas acerca del mundo de **python!**. Este es solo el principio:purple_heart:

--------
#### Puedes apoyar mi trabajo haciendo "☆ Star" en el repo. ¡Gracias!

 ### Hola, mi nombre es Harold Sabogal.
### Estudiante del SENA

![GitHub Followers](https://img.shields.io/github/followers/dst3v3n?style=social)
![GitHub Followers](https://img.shields.io/github/stars/dst3v3n?style=social)

Soy estudiante del SENA desde hace dos año. Este años estoy aprendiendo sobre Analisis y Desarrollo de Software (ADSO) como lo he comentado anteriormente. Quiero seguir aprendiendo mas sobre el mundo del Desarrollo de software **[@dst3v3n](https://github.com/dst3v3n)**.

### En mi perfil de GitHub tienes más información

[![Web](https://img.shields.io/badge/Guthub-dst3v3n-802DBF?style=for-the-badge&logo=github&logoColor=802DBF&labelColor=black)](https://github.com/dst3v3n)
