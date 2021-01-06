'''
from random import randint
rand = 0
numero = 1
x = 0
while rand != numero:
    rand = randint(0, 10)
    print(rand)
    numero = int(input("Adivinhe o número de 0 a 10: "))
    if numero != rand:
        x +=1
        print("Errou!")
    else: print("Parabéns você Acertou! Você acertou na {}º tentativa".format(x))
'''
#Correção.
from random import randint
computador = randint(0, 10)
acertou = False
palpites = 0
print(computador)
while not acertou:
    jogador = int(input("Qual é seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True

print("Parabéns você Acertou! Você acertou na {}º tentativa".format(palpites))