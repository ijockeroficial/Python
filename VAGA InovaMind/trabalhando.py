def anoTrabalhando(anos):
    print("_" * 50)
    antes = []
    depois = []
    for y, z in enumerate(anos):
        if y == 0:
            ano_ultimo_aposentado = ano_primeiro_aposentado = z[1]
        else:
            if z[1] > ano_ultimo_aposentado:
                ano_ultimo_aposentado = z[1]
            if z[1] < ano_primeiro_aposentado:
                ano_primeiro_aposentado = z[1]
        metade = ano_ultimo_aposentado - (ano_ultimo_aposentado - ano_primeiro_aposentado) / 2
    for y, z in enumerate(anos):
        if z[1] <= metade:
            antes.append(1)
        else:
            if z[1] >= metade:
                depois.append(1)
    if len(antes) > len(depois):
        print(f"A maioria das pessoas trabalharam entre os anos de {ano_primeiro_aposentado} e {metade}")
    else:
        if len(depois) > len(antes):
            print(f"A maioria das pessoas trabalharam entre os anos de {metade} e {ano_ultimo_aposentado}")




lista = [[1993, 2030], [2000, 2060], [1940, 1990], [1999, 2020]]
anoTrabalhando(lista)