import random

list=[]
resta=[]
suma=0
tam=int (random.randint(10,20))
print(tam)
for i in range(tam):
    num=int(random.randrange(100))
    list.append(num)
    suma+=num
    

media=suma/tam
resta=[list(-1)]

print(list)
print(suma)
print(f"La media es: {media}")
print(resta)
