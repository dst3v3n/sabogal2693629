from sys import path

path.append("..\\sabogal2693629")

from objetos.Persona import *

ob1 = Persona("Harold",102866)

ob1.setNombre ("Sabogal")

ob1.setDocumento (10286609)

print(ob1.getNombre ())
print(ob1.getDocumento ())

x=1

while x!="0":
    x=input("Digita un curso: ")
    if x!="0":
        ob1.Cursos(x)


y=input("Digita el curso que quieres modificar: ")
q=input("Digita el nombre de la actualizacion del curso: ")
ob1.Modificar(y,q)

v=input("Digita el curso que quieres eliminar: ")

ob1.eliminar(v)

print(ob1.Consultcursos())