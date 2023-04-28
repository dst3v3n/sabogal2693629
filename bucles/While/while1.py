#Crear un algoritmo que imprima por pantalla los numeros del 1 hasta el 10
#Asignamos las variables necesarias en este caso es i y sum
i=1
sum=0
#usamos el bucle while con una expresion.
#Si i es menor o igual a 10 va a cumplir unas lineas de codigo
#Va a imprimir el numero que tiene i y va estar sumando la variable sum y la variable i
#Cumplida la expresion el programa se saldra del bucle y imprimira en pantalla el total de la suma
while i<=10:
    print(i)
    sum+=i #sum=sum+i
    i+=1 #i=i+1
print('la suma es:',sum)

#Crear un algoritmo que imprima por pantalla los numeros del 1 hasta el 10 y se imprima las suma de los numeros impares y los numeros pares 
#Asignamos las variables necesarias en este caso es i y las variables de impares y pares, que en este caso es sp y si cada variables tiene un valor de 0
i=0
sp,si=0,0
#usamos el bucle while con una expresion.
#Si i es menor o igual a 10 va a cumplir unas lineas de codigo
#Va a tener una condicion y es que si el modulo i de la division de 2 es igual a 0
#Se va a guardar el valor en sp y se va a sumar i con sp
#De lo contrario se va a guardar el valor en la variables si, sumando si y i
#la variable i se va a sumar a si misma más 1, es decir i=i+1
# Va a seguir ese bucle hasta que el valor de i supere la expresion. Cuando i supere el numero 10
# Se imprimira por pantalla la suma de los numeros pares y los numeros impares 
while i<=10:
    print(i)
    if i%2==0:
        sp+=i
    else:
        si+=i
    i+=1
print('la suma de los pares es:',sp)
print('la suma de los impares es:',si)
