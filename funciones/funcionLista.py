import random #Importamos el modulo random
#Definimos una funcion en la cual tiene el nombre de "llenarLista" en la cual tiene dos parametros que es el tamaño y el rango
#En la funcion tiene una variable de tipo lista. Usamos composicion para que llene la lista dependiendo de los argumento que el usuario digite
#Retornamos lista
def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista

#Definimos una funcion en la cual tiene el nombre de "sumaLista" en la cual tiene un parametro que es la lista en la cual la funcion hara su funcion de sumar
#Los valores de la lista.
#La funcion tiene una varaible llamada sum que tiene un valor de 0, tambien la funcion tiene un ciclo for en la cual se encarga de que pase por cada valor de la lista
#Para poder asi sumarlos
#Retorna la variable suma
def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

#Definimos una funcion en la cual tiene como parametro una lista. La funcion se encarga de sacar el promedio de la lista
#Retornamos la funcion suma en la cual ponemos el parametro lista divido entre el tamaño de la lista
def promedioLista(lista):
    return sumaLista(lista)/len(lista)
    
l1=llenarLista(3,10) #Creamos la variable lista con los argumentos que exige la funcio llenarLista
print(l1) #Imprimimos la lista
print(sumaLista(l1)) #Imprimimos la funcion lista con el argumento de la variable ista
print(round(promedioLista(l1),2)) #Imprimos el promedio de lista pero con dos decimales. Que es lo que le pedimos a la funcion round