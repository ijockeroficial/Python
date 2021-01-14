def validaSequencia(texto):
    parenteses = []
    colchetes = []
    chaves = []
    for simb in texto:
        if simb == "(":
            parenteses.append("(")
        elif simb == ")":
            if len(parenteses) > 0:
                parenteses.pop()
            else:
                parenteses.append(")")
                break
        if simb == "[":
            colchetes.append("[")
        elif simb == "]":
            if len(colchetes) > 0:
                colchetes.pop()
            else:
                colchetes.append("]")
                break
        if simb == "{":
            chaves.append("{")
        elif simb == "}":
            if len(chaves) > 0:
                chaves.pop()
            else:
                chaves.append("}")
                break
    verifica = len(parenteses) + len(colchetes) + len(chaves)
    if verifica == 0:
        print("É uma sequência válida!")
    else: print("É uma sequência inválida!")


txt = str(input("Digite  () parenteses, {} chaves ou [] colchetes: ")).strip()
validaSequencia(txt)
