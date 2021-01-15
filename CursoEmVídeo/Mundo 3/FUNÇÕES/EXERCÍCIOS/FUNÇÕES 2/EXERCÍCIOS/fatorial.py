def fatorial(n, show=False):
    '''
    Calcula o fatorial de um numero.
    Uso: fatorial(numero, show=True)
    Param n: e o numero que vc quer descobrir o fatorial.
    Param show: (opcional) Mostrar ou nao a conta.
    return: O valor do Fatorial de um número n.
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=" ")
            if c > 1:
                print(' x ', end=" ")
            else:
                print(' = ', end=" ")
        f *= c
    return f
print(fatorial(5, show=True))
