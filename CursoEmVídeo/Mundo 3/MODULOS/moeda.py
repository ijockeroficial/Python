def aumentar(dado=0):
    dado += 1
    return print(dado)


def diminuir(dado=0):
    dado -= 1
    return print(dado)


def dobro(dado=0):
    dado *= 2
    return print(dado)


def metade(dado=0):
    dado = dado / 2
    return print(dado)


def formata(dado=0, moeda='R$'):
    return print(f"{moeda}{dado}".replace('.', ','))
