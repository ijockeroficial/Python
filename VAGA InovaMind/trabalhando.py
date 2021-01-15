def anosTrabalhando(anos):
    print("_" * 50)
    for x, y in enumerate(anos):
        if x == 0:
            primeiro = y[0]
        else:
            if y[0] < primeiro:
                primeiro = y[0]



lista = [[1993, 2030], [1980, 2020], [1940, 1990], [2003, 2070]]
anosTrabalhando(lista)