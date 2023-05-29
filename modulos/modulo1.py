from random import randint, randrange

print(randint(1,randrange(30)))

def randint (num1,num2):
    cont=0
    for i in range (num1,num2):
        cont+=1
        while cont==25:
            num3=i
            return num3


print(randint(5,30))