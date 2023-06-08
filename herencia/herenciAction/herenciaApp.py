from Aprendiz import * #Se importa el modulo Aprendiz
from Curso import * #Se importa el modulo curso

objeto=Aprendiz("Ana Kurnikova",123456,'ADSO',2693629) #Se instancia el objeto con la clase Aprendiz y se le da como nombre al objeto "objetos" 
#print(objeto.__dict__) #Se imprime los atributos del objeto
objcurso=Curso("Programacion Software","tecnico") #Se instancia un objeto de la clase Curso y se le da como nombre al objeto "objcurso"
objeto.agregarCurso(objcurso) #se llama un modulo agregaCurso. El modulo se encarga de agregar cursos a una lista
#print(objeto.__dict__) #Se imprime los atributos del objeto
objeto.componerCurso()  #Se llama un modulo que esta en la clase Aprendiz, lo que hace el modulo es pedirle que ingrese por pantalla unos valores y los añade a una lista
objeto.componerCurso()  #Se llama un modulo que esta en la clase Aprendiz, lo que hace el modulo es pedirle que ingrese por pantalla unos valores y los añade a una lista
#print(objeto.verCursos())  # lo que hace el modulo es retornar la lista del objeto y lo imprime por la funcion

#Lo que hace el ciclo es que va a para por cada valor de la lista y los va a imprimir 

for cursito in objeto.verCursos():
    print(cursito.getNombre())