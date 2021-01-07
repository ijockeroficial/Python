lista = []
boletim = []
valor = True
while valor:
    nome = str(input("Digite seu nome: ")).strip().upper()
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))
    lista.append(nome)
    lista.append(nota_1)
    lista.append(nota_2)
    boletim.append(lista[:])
    lista.clear()
    continuar = str(input("Quer continuar? S/N ")).strip().upper()
    if continuar == "S":
        valor = True
    else:
        if continuar == "N":
            valor = False
for x, y in enumerate(boletim):
    média = 0
    média = (y[1] + y[2]) / 2
    print(f"A nota média de {y[0]} é: {média}")
while True:
    nome_aluno = str(input("Digite o nome do aluno para ver sua nota: ")).strip().upper()
    for z, p in enumerate(boletim):
        if nome_aluno == p[0]:
            print(f"Nota 1: {p[1]}  /// Nota 2: {p[2]}")
    cont = str(input("Quer ver a nota de outro aluno? S/N ")).strip().upper()
    if cont == "N":
        break
