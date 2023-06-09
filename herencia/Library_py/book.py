class Book:
    def __init__(self, Titulo:str, Autor:str , ISBN:int , Publicacion:str , Status:str):
        self.__titulo_autor ={Titulo:Autor}
        self.__titulo = Titulo
        self.__autor = Autor
        self.__isbn = ISBN
        self.__publicacion = Publicacion
        self.__duet = {Titulo : []}
        self.__status = Status
        self.__comentario = {Titulo: None}
        
    def set_titulo(self,titulo:str , Autor:str):
        self.__titulo_autor.update({titulo:Autor})              

    @property
    def get_titulo(self):
        return self.__titulo_autor.keys()
    
    @property
    def get_titulos(self):
        return self.__titulo_autor.keys()
    
    @property
    def get_autor(self):
        return self.__titulo
    
    @property
    def get_autors(self):
        return self.__autor

    def  set_isbn(self,isbn):
        self.__isbn = isbn
    @property
    def get_isbn(self):
        return self.__isbn

    def set_publicacion(self,publicacion):
        self.__publicacion = publicacion

    @property
    def get_publicacion(self):
        return self.__publicacion
    
    def append_duet (self , Titulo:str , Autor:str):
        if Titulo in self.__titulo_autor:
            self.__duet.update ({self.__titulo : [self.__autor , Autor]})
            return self.__duet

    def reservation_status(self, Titulo):
        if Titulo in self.__titulo:
            return self.__status
        
    def feedback (self , Titulo:str):
        if Titulo in self.__titulo:
            comentario = input("Digita tu comentario: ")
            self.__comentario.update({self.__titulo : comentario})
            print(self.__comentario)
    
    def Book_request(self, Titulo:str):
        if Titulo in self.__titulo:
            if Book.reservation_status(self, Titulo) == "Disponible":
                print("Quieres reservarlo ")
                print("1-Si")
                print("2-No")
                selector=input("Digite la opcion: ")
                match selector:
                    case "1":
                        self.__status = "Reservado"
                        return self.__status
                    case "2":
                        return "No ha sido resevado"
                    
    def renw_info (self, Titulo):
        if Titulo in self.__titulo_autor:
            print (self.__titulo_autor, self.__isbn , self.__duet, self.__publicacion , self.__status)