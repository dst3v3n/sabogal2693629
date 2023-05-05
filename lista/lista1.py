#[] {} () 
x=100 #Se declara una variable con un valor de 100
print('tipo de x',type(x)) #Se imprime el tipo de dato que guarda esa variables
lista=[1,1.4,'sena',['a','b',],'soacha'] #Se crea una variable de tipo lista. Esa lista guarda unos valores de diferentes tipos
print(f'elemento {lista[4]}')  #Se imprime el numero cuatro de esa lista en la cual es "Soacha"
print(len(lista)) #Se imprime el tamaño de esa lista
print('tipo de lista',type(lista)) #Se imprime el tipo de datos de esa variable
print('ultimo indice',lista[-1]) #Se imprime el ultimo valor de esa lista

print(len(lista)) # Se imprime el tamaño de esa lista
lista.append(20) # Se agrega o añade un nuevo valor con el modulo append
lista.append('python') # Se agrega o añade un nuevo valor con el modulo append
print(lista) #Se imprime la lista
lista.insert(len(lista),'java') #Se agrega o añade un nuevo valor en el cual le esta indicando al codigo que debe guardarse en el valor que de la funcion len
print(lista) #Se imprime la lista
