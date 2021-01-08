from random import randint
from time import sleep
from operator import itemgetter
#CORREÇÃO
jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
for x, y in jogo.items():
    print(f"O {x} tirou {y} no dado.")
    sleep(1)
ranking = list()
#O comando: key=itemgetter(1) Pega a posiçao 1 do dicionário (o "randint(1, 6)" no caso).
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("_" * 50)
for i, v in enumerate(ranking):
    print(f"{i+1}º lugar: {v[0]} com {v[1]}.")
    sleep(1)

'''
from random import randint
resultado = {}
for x in range(0, 4):
    jogar = str(input("Jogar dado? S/N ")).strip().upper()
    if jogar == "S":    
        resultado[x] = randint(1, 6)
    else:
        break
print(resultado)
'''