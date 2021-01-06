texto = str(input("Digite uma expressao entre () parenteses: "))
print(texto)
pilha = []
for símb in texto:
    if símb == "(":
        pilha.append("(")
    elif símb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("Sua expressao está válida!")
else: print("Sua expressao está inválida!")

# A função strip() remove os espaços antes e depois do texto.
# A função split() separa os itens a partir do q for passado 
# Ex: split("A") toda vez q tiver um A vai separar a string
