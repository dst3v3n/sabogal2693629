class Account:
    def __init__(self , No_Libros_Reservados:str , No_Libros_Devueltos):
        self.__no_libros_reservados = [No_Libros_Reservados]
        self.__no_libros_devueltos = [No_Libros_Devueltos]
        self.__no_libros_perdidos = []
        self.__multa_cantidad = 0
        self.__perdido = 0


    def setLibros_Reservados (self, NO_Libros_Reservados:str):
        self.__no_libros_reservados.append(NO_Libros_Reservados)
    
    def setLibros_Devueltos (self, NO_Libros_Devueltos:str):
        self.__no_libros_devueltos.append(NO_Libros_Devueltos)
    
    def setLibros_Perdidos (self, NO_Libros_Perdidos:str):
        self.__no_libros_perdidos.append(NO_Libros_Perdidos)

    def setMulta_Cantidad (self, NO_Libros_Cantidad:str):
        self.__multa_cantidad = NO_Libros_Cantidad
    
    def setPerdido(self,perdidos):
        self.__perdido = perdidos

      
    @property
    def getNo_Libros_Reservados (self):
        numero = len(self.__no_libros_reservados)
        return {numero : [self.__no_libros_reservados] }

    @property
    def getNo_Libros_Devueltos (self):
        numero = len(self.__no_libros_devueltos)
        return {numero : [self.__no_libros_devueltos] }
    
    @property
    def getNo_Libros_Perdidos (self):
        numero = len(self.__no_libros_perdidos)
        return {numero: [self.__no_libros_perdidos]}

    @property
    def getMulta_Cantidad (self):
        return self.__multa_cantidad
    
    def calculate_fine (self, perdido):
        self.__multa_cantidad = perdido
        multa = (1160000 * 0.03) * self.__multa_cantidad
        return multa