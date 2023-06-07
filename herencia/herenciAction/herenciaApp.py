from Aprendiz import * #Se importa el modulo Aprendiz
from Curso import * #Se importa el modulo curso

objeto=Aprendiz("Ana Kurnikova",123456,'ADSO',2693629) #Se instancia el objeto con la clase Aprendiz y se le da como nombre al objeto "objetos" 
#print(objeto.__dict__)
objcurso=Curso("Programacion Software","tecnico")
objeto.agregarCurso(objcurso)
#print(objeto.__dict__)
objeto.componerCurso()
objeto.componerCurso()
#print(objeto.verCursos())
for cursito in objeto.verCursos():
    print(cursito.getNombre())