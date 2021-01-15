def anosTrabalhando(anos):
    print("_" * 50)
    '''
    for x, y in enumerate(anos):
        if x == 0:
            primeiro = y[0]
            ultimo = y[1]
        else:
            if y[0] < primeiro:
                primeiro = y[0]
            if y[1] > ultimo:
                ultimo = y[1]
    '''


lista = [[1993, 2030], [1980, 2020], [1940, 1990], [2003, 2070]]
anos = {}
for pessoa in lista:
    for anos_trabalhados in range(pessoa[0], pessoa[1] + 1):
        if anos_trabalhados in anos:
            anos[anos_trabalhados] += 1
        else: 
            anos[anos_trabalhados] = 1
print(anos)
