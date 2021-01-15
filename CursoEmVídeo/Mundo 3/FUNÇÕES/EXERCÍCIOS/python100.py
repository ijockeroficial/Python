from random import randint
numeros = list()
def sorteia(lista):
    x = 0
    while x < 5:
        x += 1
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
        else:
            x -= 1
    print(f"Números sorteados {lista}")


def somaPar(lista):
    par = list()
    soma = 0
    for x in lista:
        if x % 2 == 0:
            soma += x
            par.append(x)

    print(f"A soma dos números pares são: {soma} ")
    print(f"Os números pares sorteados foram: {par} ")


sorteia(numeros)
somaPar(numeros)
