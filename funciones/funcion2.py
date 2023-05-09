
def potenciacion (x,y):
    while x!= 0:
        x=int(input("Digita el numero base: "))
        y=int(input("Digita el exponente: "))
        operacion=x**y

        if y!=0:
            print(f"El resultado de esa operacion es: {operacion}")
        else:
            print("Haz salido exitosamente")



x=1
y=1
potenciacion (x,y)