#CORREÇÃO
jogador = dict()
partidas = list()

jogador['nome'] = str(input("Nome do Jogador: "))
tot = int(input(f"Quantas partidas o {jogador['nome']} jogou? "))

for c in range(0, tot):
    partidas.append(int(input(f"    Quantos gols na partida {c}? ")))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print("_" * 50)
print(jogador)
print("_" * 50)

for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print("_" * 50)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas.")

for b, c in enumerate(jogador['gols']):
    print(f"Na partida {b}, fez {c} gols.")
print(f"Foi um total de {jogador['total']} gols.")
'''
#Fiz assim:
jogador = {} #Cria um dicionário chamado "jogador".
jogador["nome"] = str(input("Nome: "))
jogador["partidas"] = int(input("Partidas: "))
gols = [] #Cria uma lista chamada "gols".
#Percorre a quantidade de partidas
for x in range(0, jogador["partidas"]):
    gols.append(str(input(f"Gols na {x+1}º partida: ")))
jogador["gols"] = gols[:]
total = 0
#Calcula a quantidade total de gols.
for z in gols:
    total += int(z)
jogador["total"] = total
print("_" * 50)
#Apresenta na tela
for t, v in jogador.items():
    print(f"{t}: {v}")
'''