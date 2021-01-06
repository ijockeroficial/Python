from random import randint
numeros = []
lista = []
jogos = int(input("Quantos jogos vc quer gerar? "))
y = 1
while y <= jogos:
    x = 0
    while x <= 5:
        x += 1
        numero = randint(1, 60)
        if numero not in numeros:
            numeros.append(numero)
        else: 
            x -= 1
    if numeros not in lista:
        lista.append(numeros[:])
        numeros.clear()
        y += 1

print(lista)

