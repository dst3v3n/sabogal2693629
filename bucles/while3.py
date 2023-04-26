#Hacer un algoritmo que el usuario digite los numeros y caundo digite el 0 se sale del programa
#El sistema debe contar los numeros que el usuario digito, menos el cero
#El sistema debe sumar los numeros digitados
#Sacar el promedio sin contar el numero 0
#Mostrar cual es el numero mayor y el numero menor

#Se les asiga las variables 
num=1 #Esta variable se encargara de guardar los numeros digitados por el usuario
cont=0 #Esta variable se encarga de contar las veces que el usuario digito los numeros sin el cero
sum=0 #En esta variable vamos a sumar los numeros 
prom=0 #En esta variable va hacer para el promedio
menor=10000000000000 #En esta variable se guarda el menor
mayor = 0 #En esta variable se encarga se guardar el mayor

#El bucle while dice que si el numero es diferente de 0 entonces el sistema.
#El sistema le debe pedir que digite numeros
#El sistema contara los numeros digitados por el usuario
#El sistema sumara los numeros que ha digitado el usuario
#Tiene dos condiciones para mayor y menor
while num!=0:
    num=int(input('ingrese numero'))
    cont=cont+1 #cont+=1
    sum+=num
    if num>mayor:    
        mayor=num
    if num<menor and num!=0:
        menor=num
        
#El sistema disminuira un numero para que el 0 no se cuente
cont-=1
#Para sacar el promedio necesitamos de esa expresion 
prom=sum/cont

#Se imprime los resultados
print("La suma de los numeros es: " , sum)
print("La promedio de los numeros es: " , prom)
print(f'El usuario ingreso {cont} numeros ')
print("El numero mayor es: " , mayor)
print("El numero menor es: " , menor)
#print('El usuario ingreso', cont, 'numeros')
