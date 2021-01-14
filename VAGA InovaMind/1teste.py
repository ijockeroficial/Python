def validaSequencia(texto):
    parenteses = []
    colchetes = []
    chaves = []
    for simb in texto:
        if verificaCaractere(simb, parenteses, "(", ")"):
            break
        if verificaCaractere(simb, colchetes, "[", "]"):
            break
        if verificaCaractere(simb, chaves, "{", "}"):
            break

    verifica = len(parenteses) + len(colchetes) + len(chaves)
    if verifica == 0:
        print("É uma sequência válida!")
    else: print("É uma sequência inválida!")


def verificaCaractere(simb, lista, c1, c2):
    if simb == c1:
            lista.append(c1)
    elif simb == c2:
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(c2)
            return True
    return False


txt = str(input("Digite  () parenteses, {} chaves ou [] colchetes: ")).strip()
validaSequencia(txt)
