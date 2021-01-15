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
    teste = []
    for x in sorted(anos.items(), key=itemgetter(1), reverse=True):
        teste.append(x[1])
    a = max(teste, key=int)
    print(a)
    lista_nova = []
    for x in sorted(anos.items(), key=itemgetter(1), reverse=True):
        if x[1] == a:
            lista_nova.append(x[0])
    print(f"Houve mais pessoas trabalhando no(s) ano(s) de: {lista_nova}")

    
lista = [[1993, 2005], [1993, 2005], [1993, 2005], [2006, 2070], [2006, 2070]]
anosTrabalhando(lista)
