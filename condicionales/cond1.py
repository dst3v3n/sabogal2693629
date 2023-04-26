#Crear un programa que pida al usuario que digite dos numero.
#El programa debe imprimir por pantalla si los numero son iguales, descendentes o ascendentes

#Para resolver el programa se debe crear dos variables donde se guardaran esos dos numero, con un input para que el usuario digite los numerps

x=input('ingrese numero')
y=input('ingrese numero')

#Usaremos las condicionales if, elif y else
#En el if usaremos la expresion que si los numero asignados son iguales imprima por pantalla "Son iguales"  x==y
if x==y:
    print('son iguales')

#Si no se cumple el if vamos a usar elif. Si x es mayor que y, si se cumple el sistema va a imprimir por pantalla que son "Descendente"     
elif x>y:
    print('descendente')
#Si no se cunple esas dos condiciones el sistema va a imprimir por pantalla que los numeros son "Ascendente"
else:
    print('ascendente')