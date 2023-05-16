# Llenar un arreglo con la serie de Fibonacci, con la cantidad de dígitos que el usuario
# indique al inicio del programa.

def fibo(lista,x):
    a=0
    b=1
    for i in range(x):
        c=a+b
        a=b
        b=c
        lista.append(b)
    return lista

y=abs(int(input("Digita la cantidad de valores para el fibonacci: ")))
lista=[]

print(fibo(lista,y))