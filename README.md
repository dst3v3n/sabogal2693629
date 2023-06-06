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
| 10  |  [Pruebas Modulos](./pruebas/modulos)|
| 11  |  [Pruebas Objetos](./pruebas/objetos/)|

--------
## **Ultimos codigos realizados** :purple_heart:

>Programación Orientada a Objetos

```python
class Empleado:
    counter = 0
    def __init__(self , Nombre:str , Cargo:str ,Salario:int):
        self.__nombre = Nombre
        self.__cargo = Cargo
        self.__salario = Salario
        self.__horas = 0
        Empleado.counter += 1

    def getNombre (self , Nombre:str):
        self.__nombre = Nombre
        
    def getCargo (self , Cargo:str):
        self.__cargo = Cargo
    
    def getSalario (self , Salario:int):
        self.__salario = Salario
    
    @property
    def setNombre (self):
        return self.__nombre
    
    @property
    def setCargo (self):
        return self.__cargo
    
    @property
    def setSalario (self):
        return self.__salario

    def Salario_Hora (self):
        hora = self.__salario/(47*4)
        return int(hora)

    def incrementoSalario (self):
        if self.__salario == 1160000:
            ipc = 0.1312 + 0.03
            incremento = self.__salario * ipc
            total_incremento = self.__salario + incremento
            return int(total_incremento)
        else: 
            total_incremento = self.__salario * 0.1312
            return int(total_incremento)
        
    def hora_extras (self, Horas:int =0):
        self.__horas = Horas
        incremento = Empleado.incrementoSalario(self)
        salario = Empleado.Salario_Hora(self)
        extras = salario * Horas
        total = incremento + extras
        return int(total)
    
    def sueldo_total (self):
        total = Empleado.hora_extras(self , self.__horas)
        return total
```
>El codigo se encuentra **[Aqui](./objetos/Empleado.py)**

--------
>Instanciando los objetos



```python
from sys import path

path.append("..\\sabogal2693629")

from objetos.Empleado import *

persona1 = Empleado ("Harold" , "ADSO" , 120000)

persona1.getNombre ("Steven")
persona1.getCargo ("Multimedia")
persona1.getSalario (1160000)

print(persona1.setNombre)
print(persona1.setCargo)
print(persona1.setSalario)

print(persona1.Salario_Hora())
print(persona1.incrementoSalario())
print(persona1.hora_extras(2))
print(persona1.sueldo_total())




persona2 = Empleado ("Jhonatan" , "Multimedia" , 120000)

persona2.getNombre ("Sabogal")
persona2.getCargo ("Sistemas")
persona2.getSalario (2460000)

print(persona2.setNombre)
print(persona2.setCargo)
print(persona2.setSalario)

print(persona2.Salario_Hora())
print(persona2.incrementoSalario())
print(persona2.hora_extras(1))
print(persona2.sueldo_total())




persona3 = Empleado ("Jhonatan" , "Multimedia" , 5000000)

persona3.getNombre ("Sabogal")
persona3.getCargo ("Sistemas")
persona3.getSalario (5500000)

print(persona3.setNombre)
print(persona3.setCargo)
print(persona3.setSalario)

print(persona3.Salario_Hora())
print(persona3.incrementoSalario())
print(persona3.sueldo_total())

print(persona3.counter)
```
>El codigo se encuentra **[Aqui](./pruebas/objetos/EmpleadoAPP.py)**

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
