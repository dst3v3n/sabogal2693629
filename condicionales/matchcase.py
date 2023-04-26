#Crear un programa que imprima las opciones de sumar, restar, multiplicar y dividir.
#El usuario digitara un numero de acuerdo a las opciones 

#Creamos dos variables en cual digitaremos los valores que queremos que se guarden esas variables 

num1,num2=100,25
#El sistema va imprimir las opciones con unos numero en el cual servira para que el usuario seleccione que opcion quiere
print('1-sumar')
print('2-restar')
print('3-multiplicar')
print('4-dividir')
#El usuario digitara un numero del 1 al 4 dependiendo de lo que quiere hacer con los valores que estan guardados en las respectivas vaiables
selector=(input('Digite la opcion'))
#Ya digitado el numero el sistema usara dos palabras reservadas importantes que son match y case
#Match y case sirven para simplificar las condicionales 
#La sintaxis es muy facil. Primero se pone la palabra reservada "Match" despues la variable a la que queremos que se cumplan las condiciones
#Despues vamos a usar el case con la expresion de la condicion. Ojo el case debe tener sangria
#Despues se pone el codigo sobre que va a pasar si se cumple esa condicion, tambien con sangria
#Los numeros tienen comillas simples. Esas comillas cumplen la funcion de decirle al sistema que los numeros son de tipo cadena o tambien llamado tipo strings
match selector:
    case '1':
        print(num1+num2)
    case '2':
        print(num1-num2)
    case '3':
        print(num1*num2)
    case '4':
        print(num1/num2)