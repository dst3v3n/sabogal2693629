class Persona: #Se crea una clase llamada Persona
    def __init__(self,nombre,documento):  #Se crea el contructor con dos parametros del lado del usuario que en este caso seria el nombre y el numero del documento del objeto
        self.__nombre=nombre #Se declara las variables con el valor del parametro del nombre
        self.__documento=documento #Se declara las variables con el valor del parametro del documento