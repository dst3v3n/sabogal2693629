# llenar una tupla con n elementos max 20 numeros, entre 0 y 100
#Sumar los elementos de la tupla 
import random

tamaño = random.randint(1,20)
print(tamaño)
t1=()
for i in range(tamaño):
    valores = random.randrange(100)
    t1=t1+(valores,)
print(t1)