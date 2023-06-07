class Curso: #Se crea una clase llamada Curso
    def __init__(self,nombre,tipo): #Se crea un constructor con dos parametros del lado del servidor que en este caso son el nombre del curso y el tipo del curso
        self.__nombre=nombre #Se declara la variable nombre y se le asigna como valor el parametro nombre
        self.__tipo=tipo #Se declara la variable tipo y se le asiga como valor el parametro tipo

    def getNombre(self): #Se crea un metodo (Funcion) llamada "getNombre" en el cual del lado del programador se le da como atributo self. Del lado del usuario no pide ningun argumento
        return self.__nombre #Se retorna un la variable llamada "self.__nombre"