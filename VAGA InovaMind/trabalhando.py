from operator import itemgetter
def anosTrabalhando(lista):
    print("_" * 50)
    anos = {}
    for pessoa in lista:
        for anos_trabalhados in range(pessoa[0], pessoa[1] + 1):
            if anos_trabalhados in anos:
                anos[anos_trabalhados] += 1
            else: 
                anos[anos_trabalhados] = 1
    for x in sorted(anos.items(), key=itemgetter(0)):
        print(x[1])



lista = [[1993, 2030], [1980, 2020], [1940, 1990], [2003, 2070]]
anosTrabalhando(lista)
