#Crear un algoritmo que pida numeros, debe mirar si los numeros son factore
#Sino son factores debe pedirle que vuelva a digitar otros dos numeros
#Si los numeors son factores  debe imprimir por pantalla "Son factor"

#Declaramos dos variables x que tiene valor de 5 y y que vale 3
x=5
y=3

#Usamos el bucle while con la expresion de que si x y y  el modulo debe ser igual 0
#Usamos or para poner otra expresion en el cual es que si y y x el modulo es igual 0
#La expresion usa una palabra reservada que es "not" en el cual si alguna de las expresiones se cumple la va a convertir en falso
#Y si ninguna de las expresiones se cumple las va a convertir a True
#El bucle while va a seguir hasta que los numeros sean factores
#Salido del bucle el sistema imprimira que los numero "Son factor"

while not (x%y==0 or y%x==0):    
    print('Rutina para saber si dos numeros son factores')
    x=int(input('ingrese numero')) 
    y=int(input('ingrese numero'))  
print('Son factor')