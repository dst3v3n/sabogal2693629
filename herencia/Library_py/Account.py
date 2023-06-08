class Account:
    def __init__(self , NO_Libros_Prestado:str , No_Libros_Reservados:str , No_Libros_Devueltos:str):
        self.__no_libros_prestados = [NO_Libros_Prestado]
        self.__no_libros_reservados = [No_Libros_Reservados]
        self.__no_libros_devueltos = [No_Libros_Devueltos]
        self.__no_libros_perdidos = []
        self.__multa_cantidad = 0

    def setLibros_Prestados (self, NO_Libros_Prestados:str):
        self.__no_libros_prestados = NO_Libros_Prestados
    
    def setLibros_Reservados (self, NO_Libros_Reservados:str):
        self.__no_libros_reservados = NO_Libros_Reservados
    
    def setLibros_Reservados (self, NO_Libros_Devueltos:str):
        self.__no_libros_devueltos = NO_Libros_Devueltos
    
    def setLibros_Reservados (self, NO_Libros_Perdidos:str):
        self.__no_libros_perdidos = NO_Libros_Perdidos

    def setMulta_Cantidad (self, NO_Libros_Cantidad:str):
        self.__multa_cantidad = NO_Libros_Cantidad

    @property
    def getLibros_Prestados (self):
        return self.__no_libros_prestados
    
    @property
    def getLibros_Reservados (self):
        return self.__no_libros_reservados
    
    @property
    def getLibros_Devueltos (self):
        return self.__no_libros_devueltos
    
    @property
    def getLibros_Perdidos (self):
        return self.__no_libros_perdidos
    
    @property
    def getMulta_Cantidad (self):
        return self.__multa_cantidad
    
    def calculate_fine (self):
        contador = 0
        for i in self.__no_libros_perdidos:
            contador += 1
        if contador != 0:
            multa = (1160000 * 0.03) * contador
        return multa