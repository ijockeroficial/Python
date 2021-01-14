def anoTrabalhando(anos):
    print("_" * 50)
    print("Apresentando os anos de inicio e fim: ")
    print(anos)
    for x, y in enumerate(anos):
        cont = y[1] - y[0]
        print(cont)
    

  
lista = [[1990, 2030], [2000, 2060]]
anoTrabalhando(lista)