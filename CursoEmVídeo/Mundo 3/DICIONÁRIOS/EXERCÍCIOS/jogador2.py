jogador = dict()
partidas = list()
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do Jogador: "))
    tot = int(input(f"Quantas partidas o {jogador['nome']} jogou? "))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f"    Quantos gols na partida {c}? ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar? S/N ")).upper()[0]
        if resp in "SN":
            break
        print("ERRO! Responda apenas S ou N")
    if resp == "N":
        break
print("cod ", end=" ")
for i in jogador.keys():
    print(f"{i:<15}", end=" ")
print("_" * 50)
for k, v in enumerate(time):
    print(f"{k:>4}", end=" ")
    for d in v.values():
        print(f"{str(d):<15}", end=" ")
    print()
print("_" * 50)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar)"))
    if busca == 999:
        break
    if busca >= len(time):
        print("Não existe jogador com o código {busca}!")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:")
        for i, g in enumerate(time[busca]['gols']):
            print(f" No jogo {i+1} fez {g} gols.")
        print("_" * 50)
print("<< VOLTE SEMPRE >>")
