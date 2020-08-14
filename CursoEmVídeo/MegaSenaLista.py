import random

inicio = 0
resultado = []
while(inicio <= 5):
    inicio += 1
    numero = random.randrange(1,60)
    if(numero != numero):
        resultado = numero
    else: 
        resultado = numero + 1
        
print(resultado)