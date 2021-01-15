from operator import itemgetter
anos_informados = []
lista = []
valor = True
while valor:
    ano_inicio = int(input("Digite o ano que começou a trabalhar: "))
    ano_fim = int(input("Digite o ano que aposentou: "))
    if ano_inicio > 0 and ano_inicio < ano_fim and ano_fim > 0:
        anos_informados.append(ano_inicio)
        anos_informados.append(ano_fim)
        lista.append(anos_informados[:])
        anos_informados.clear()
    else:
        print("Ops! Dados inválidos")
    continuar = str(input("Quer continuar? S/N ")).strip().upper()[0]
    if continuar == "S":
        valor = True
    else:
        if continuar == "N":
            valor = False


def anosTrabalhando(lista):
    print("_" * 50)
    anos = {}
    for pessoa in lista:
        for anos_trabalhados in range(pessoa[0], pessoa[1] + 1):
            if anos_trabalhados in anos:
                anos[anos_trabalhados] += 1
            else: 
                anos[anos_trabalhados] = 1
    maior = max(anos.items(), key=itemgetter(1))[1]
    lista_nova = []
    for x in sorted(anos.items(), key=itemgetter(1), reverse=True):
        if x[1] == maior:
            lista_nova.append(x[0])
    print(f"Houve mais pessoas trabalhando no(s) ano(s) de: {lista_nova}")

anosTrabalhando(lista)